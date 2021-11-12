import pandas as pd
import numpy as np

def preprocess(df):
    # remove lines with empty qids
    df = df[~df['qids'].str.len().eq(0)]
    # take only the first qid
    df['qids'] = df['qids'].apply(lambda x: x[0]) # this gives a warning
    return df
    
def merge_df(df,parquet_df):
    return preprocess(df).merge(parquet_df, left_on = 'qids', right_on = 'id')
    
def first_qid(df):
    '''
    if df element has multiple qids, only take the first one
    '''
    return df.apply(lambda x: x[0] if x is not None else None)

def prep_df(df):
    '''
    if df element has multiple qids, only take the first one
    then name the first column 'qid'
    '''
    df = first_qid(df).to_frame().copy()
    return df.rename(columns = {df.columns[0]:'qids'})

def process_qid_chunk(chunk, qids_clean_merged):
    """
    this function processes one chunk of data
    """
    qids_clean_merged = qids_clean_merged.reindex(columns=qids_clean_merged.columns.union(chunk.columns))
    qids_clean_merged.update(chunk)
    return qids_clean_merged

def process_qid_one(path_to_file, qids_clean, chunksize = 10 ** 4):
    """
    this function processes a csv file in chunks
    here it attributes qid to their respective labels and descriptions 
    ( by joining the qid label df to the df not containing them)
    """
    qids_clean_merged = qids_clean.copy()
    qids_clean_merged['Label'] = np.NaN
    qids_clean_merged['Description'] = np.NaN
    qids_clean_merged.set_index('qids',inplace = True)
    qids_clean_merged.index.rename('QID', inplace = True)
    
    with pd.read_csv(path_to_file, compression='bz2', index_col = 'QID', chunksize = chunksize) as df_reader:
        for chunk in df_reader:
            qids_clean_merged = process_qid_chunk(chunk, qids_clean_merged)
    return qids_clean_merged

def rename_col(df,title='column_name'):
    df = df.reset_index()
    return df.rename(columns = {df.columns[1]:title}).iloc[:,1].to_frame()

def qid_to_label(merged_df, qids_onlyquotebank_path, column_names):
    for column_str in column_names:
        nationality_df = prep_df(merged_df[column_str])
        nationality_df = process_qid_one(qids_onlyquotebank_path, nationality_df , chunksize = 10 ** 6)
        nationality_df = rename_col(nationality_df,column_str)
        merged_df[column_str] = nationality_df
    return merged_df

def check_if_qid_modified(df):
    '''
    take first term of list out of ndarray, and checks if it's a QID
    '''
    return df.str.contains(r'[Q][0-9]+').any()

def check_df_columns_if_qid(df):
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






