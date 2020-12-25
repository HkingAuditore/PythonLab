import pandas as pd

chunkSize = 5000
df_chunks = pd.read_csv('2020.csv', header=0, encoding="utf-8", chunksize=chunkSize,
                        iterator=True)
chunks = []
j = 0

while True:
    try:
        chunk = df_chunks.get_chunk(chunkSize)
        chunks.append(chunk)
        print(j)
        j += 1
    except StopIteration:
        break

df = pd.concat(chunks, ignore_index=True)


def count_multi_selections(str):
    all_selections = []
    for i in df.index:
        try:
            selection = df.loc[i, str]
            selections = selection.split(';')
            # print(dbs)
            for cur_selection in selections:
                if all_selections.count(cur_selection) == 0:
                    all_selections.append(cur_selection)
        except:
            continue
    print(all_selections)
    return all_selections


databaseWorkedWith = count_multi_selections('DatabaseWorkedWith')

def generate_multi_selections(list,str):
    for i in df.index:
        try:
            selection = df.loc[i, str]
            selections = selection.split(';')
            # print(dbs)
            for cur_selection in selections:
                if all_selections.count(cur_selection) == 0:
                    all_selections.append(cur_selection)
        except:
            continue
    print(all_selections)
    return all_selections


# count_multi_selections('LanguageWorkedWith')
# count_multi_selections('MiscTechDesireNextYear')
# count_multi_selections('DatabaseWorkedWith')

df.to_csv('2020_edit.csv', encoding="utf-8", index=False)
