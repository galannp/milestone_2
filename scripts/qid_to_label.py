import pandas as pd
import numpy as np

def preprocess(df):
    '''
    Remove the rows containing empty qid entries ( so no authors) and when
    a tuple of QIDs is present is it replaced with it's first term
    Input : Dataframe containing selected quotes
    Output : Dataframe containing selected quotes minus rows with no authors,
            and with edited QID entries
    '''
    # remove lines with empty qids
    df = df[~df['qids'].str.len().eq(0)]
    # take only the first qid
    df['qids'] = df['qids'].apply(lambda x: x[0]) # this gives a warning
    return df
    
def merge_df(df, parquet_df):
    '''
    This function perfoms a left join on the dataframe containing our selected quotes,
    with the dataframe containing the attributes (from the parquet file). They are joined
    on the indexes 'qids' and 'id' for the dataframe attributes
    Input : 
    Output : 
    '''
    return preprocess(df).merge(parquet_df, left_on = 'qids', right_on = 'id')
    
def first_qid(df):
    '''
    If a df entry has multiple qids, this function replace it with the first one.
    Input : Pandas series containing the column we want to clean
    Output : Pandas series containing the same column but cleaned
    '''
    return df.apply(lambda x: x[0] if x is not None else None)

def prep_df(df):
    '''
    If a df entry has multiple qids, this function replace it with the first one.
    It also replaces the name of the first column to 'qid'
    Input : Pandas series containing the column we want to clean
    Output : Pandas series containing the same column but cleaned
    '''
    df = first_qid(df).to_frame().copy()
    return df.rename(columns = {df.columns[0]:'qids'})

def process_qid_chunk(chunk, qids_clean_merged):
    """
    After cleaning the dataframe containing the selected quotes, this function is used
    to merge it with a chunk of the dataframe containing qid labels ( from the provided .json.bz2 file)
    This function  iteratively merges the chunks to the same dataframe, so it will iteratively add
    the attributes available in the chunk.
    Input : chunk of the parquet file and qid column of 
    Output : dataframe
    """
    qids_clean_merged = qids_clean_merged.reindex(columns=qids_clean_merged.columns.union(chunk.columns))
    qids_clean_merged.update(chunk)
    return qids_clean_merged

def process_qid_one(path_to_file, qids_clean, chunksize = 10 ** 4):
    """
    This function processes a csv file in chunks
    here it attributes qid to their respective labels and descriptions 
    ( by joining the qid label df to the df not containing them)
    path_to_file should be replaced with the path to 'wikidata_labels_descriptions_quotebank.csv.bz2'
    or 'wikidata_labels_descriptions.csv.bz2'
    """
    qids_clean_merged = qids_clean.copy() 
    qids_clean_merged['Label'] = np.NaN # create empty columns so that iterative join is possible
    qids_clean_merged['Description'] = np.NaN
    qids_clean_merged.set_index('qids',inplace = True) 
    qids_clean_merged.index.rename('QID', inplace = True) # rename the index so that the first join is the same as the following ones
    
    with pd.read_csv(path_to_file, compression='bz2', index_col = 'QID', chunksize = chunksize) as df_reader:
        for chunk in df_reader:
            qids_clean_merged = process_qid_chunk(chunk, qids_clean_merged)
    return qids_clean_merged

def rename_col(df, title='column_name'):
    '''
    This function renames a column of a dataframe
    '''
    df = df.reset_index()
    return df.rename(columns = {df.columns[1]:title}).iloc[:,1].to_frame()

def qid_to_label(merged_df, qids_onlyquotebank_path, column_names):
    '''
    This function regroupes other functions. Every attribute column of the dataframe is joined with an extra 
    dataset ( containg the lables of the qids in quotebank ) 
    Input : merged_df still containing strings in QID format, the columns containing those strings,
    Output : merged_df where all qids are replaced 
    '''
    for column_str in column_names:
        nationality_df = prep_df(merged_df[column_str])
        nationality_df = process_qid_one(qids_onlyquotebank_path, nationality_df , chunksize = 10 ** 6)
        nationality_df = rename_col(nationality_df,column_str)
        merged_df[column_str] = nationality_df
    return merged_df

def check_if_qid_modified(df):
    '''
    This function take first term of list out of ndarray, and checks if it's a QID
    Input : Dataframe
    Output : number of occurences of QIDS in the dataframe
    '''
    return df.str.contains(r'[Q][0-9]+').any()

def check_df_columns_if_qid(df):
    '''
    This function prints if there is a string in QID format in the attribute columns and the
    number of occurences of such strings
    '''
    print('column : nationality ', check_if_qid_modified(df['nationality']))
    print('column : gender ', check_if_qid_modified(df['gender']))
    print('column : ethnic_group ', check_if_qid_modified(df['ethnic_group']))
    print('column : US_congress_bio_ID ', check_if_qid_modified(df['US_congress_bio_ID']))
    print('column : occupation ', check_if_qid_modified(df['occupation']))
    print('column : party ', check_if_qid_modified(df['party']))
    print('column : academic_degree ', check_if_qid_modified(df['academic_degree']))
    print('column : id ', check_if_qid_modified(df['id']))
    print('column : label ', check_if_qid_modified(df['label']))
    print('column : candidacy ', check_if_qid_modified(df['candidacy']))
    print('column : type ', check_if_qid_modified(df['type']))
    print('column : religion ', check_if_qid_modified(df['religion']))






