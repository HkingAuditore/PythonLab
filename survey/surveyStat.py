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


def count_multi_selections(name):
    all_selections = []
    for i in df.index:
        try:
            selection = df.loc[i, name]
            selections = selection.split(';')
            # print(dbs)
            for cur_selection in selections:
                if all_selections.count(cur_selection) == 0:
                    all_selections.append(cur_selection)
        except:
            continue
    # print(all_selections)
    return all_selections


def generate_multi_selections(list, name):
    for selection_in_list in list:
        df[name + "_" + selection_in_list] = 0
    for i in df.index:
        try:
            # print('in:'+str(i))
            selection = df.loc[i, name]
            selections = selection.split(';')
            for cur_selection in selections:
                df.loc[i, name + "_" + cur_selection] = 1
        except:
            continue
    return


def generate_multi_selections_name(name):
    selections_list = count_multi_selections(name)
    generate_multi_selections(selections_list, name)
    print(name + " End!")


multi_selections_list = [
                        'DatabaseDesireNextYear',
                        # 'DatabaseWorkedWith',
                         # 'DevType',
                         # 'JobFactors',
                         # 'LanguageDesireNextYear',
                         # 'LanguageWorkedWith',
                         # 'MiscTechDesireNextYear',
                         # 'MiscTechWorkedWith',
                         # 'NEWCollabToolsDesireNextYear',
                         # 'NEWCollabToolsWorkedWith',
                         # 'NEWJobHunt',
                         # 'NEWJobHuntResearch',
                         # 'NEWPurchaseResearch',
                         # 'NEWSOSites',
                         # 'NEWStuck',
                         # 'PlatformDesireNextYear',
                         # 'PlatformWorkedWith',
                         # 'WebframeDesireNextYear',
                         # 'WebframeWorkedWith',
                         # 'WebframeWorkedWith',
                         ]

def generate_multi_all_selections(name_list):
    for i in df.index:
        try:
            for name_in_list in name_list:
                selection = df.loc[i, name_in_list]
                selections = selection.split(';')
                for cur_selection in selections:
                    df.loc[i, name_in_list + "_" + cur_selection] = 1
            print(str(i)+" Done!")
        except:
            continue
    return

def generate_multi_selections_dataframe(name_list):
    all_list = []
    for name_in_list in name_list:
        all_list.append(count_multi_selections(name_in_list))
        print(name_in_list + str(all_list[-1]))
        for selection_name in all_list[-1]:
            df[name_in_list + "_" + selection_name] = 0
    generate_multi_all_selections(name_list)


generate_multi_selections_dataframe(multi_selections_list)
print("All End!")


df.to_csv('2020_edit_plus.csv', encoding="utf-8", index=False)
