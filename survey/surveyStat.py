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
    print(all_selections)
    return all_selections


def generate_multi_selections(list, name):
    for selection_in_list in list:
        df[name + "_" + selection_in_list] = ''
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


multi_selections_list = ['DatabaseWorkedWith',
                         'DevType',
                         'JobFactors',
                         'LanguageDesireNextYear',
                         'LanguageWorkedWith'
                         'MiscTechDesireNextYear',
                         'MiscTechWorkedWith',
                         'NEWCollabToolsDesireNextYear',
                         'NEWCollabToolsWorkedWith',
                         'NEWJobHunt',
                         'NEWJobHuntResearch',
                         'NEWPurchaseResearch',
                         'NEWSOSites',
                         'NEWStuck',
                         'PlatformDesireNextYear',
                         'PlatformWorkedWith',
                         'WebframeDesireNextYear',
                         'WebframeWorkedWith',
                         'WebframeWorkedWith',
                         ]

def generate_multi_selections_name(name):
    selections_list = count_multi_selections(name)
    generate_multi_selections(selections_list, name)
    print(name + " End!")


generate_multi_selections_name('DatabaseWorkedWith')
generate_multi_selections_name('DevType')
generate_multi_selections_name('JobFactors')
generate_multi_selections_name('LanguageDesireNextYear')
generate_multi_selections_name('LanguageWorkedWith')
generate_multi_selections_name('MiscTechDesireNextYear')
generate_multi_selections_name('MiscTechWorkedWith')
generate_multi_selections_name('NEWCollabToolsDesireNextYear')
generate_multi_selections_name('NEWCollabToolsWorkedWith')
generate_multi_selections_name('NEWJobHunt')
generate_multi_selections_name('NEWJobHuntResearch')
generate_multi_selections_name('NEWPurchaseResearch')
generate_multi_selections_name('NEWSOSites')
generate_multi_selections_name('NEWStuck')
generate_multi_selections_name('PlatformDesireNextYear')
generate_multi_selections_name('PlatformWorkedWith')
generate_multi_selections_name('WebframeDesireNextYear')
generate_multi_selections_name('WebframeWorkedWith')
generate_multi_selections_name('WebframeWorkedWith')

print("All End!")

# count_multi_selections('LanguageWorkedWith')
# count_multi_selections('MiscTechDesireNextYear')
# count_multi_selections('DatabaseWorkedWith')

df.to_csv('2020_edit.csv', encoding="utf-8", index=False)
