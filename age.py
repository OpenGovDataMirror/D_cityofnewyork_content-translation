from googletrans import Translator
import pandas as pd
import os

# Begin the translator and translate!
translator = Translator()

file = os.path.join(os.getcwd(),'age-headings.csv')
ages = pd.read_csv(file)

print(ages)

ages_df = pd.DataFrame()
ages_df['en'] = ages['en']
print(ages_df)

language_codes = [
'es',
'ht',
'fr',
'ko',
'pl',
'ru',
'bn',
'ar',
'ur',
'zh-TW'
]

for i in range(len(language_codes)):
  ages_df = pd.DataFrame()
  ages_df['en'] = ages['en']
  ages_df['slug_en'] = ages['slug_en']
  ages_df['id_en'] = ages['id_en']
  ages_df['desc_en'] = ages['desc_en']
  print(language_codes[i])

  for j in range(len(ages_df)):

    if language_codes[i] == 'zh-TW':
      ages_df.at[j, 'name'] = translator.translate(str(ages_df['en'][j]), dest=language_codes[i]).text
      ages_df.at[j, 'slug'] = ages_df.at[j,'slug_en'] + '-zh-hant'
      ages_df.at[j, 'desc'] = translator.translate(str(ages_df['desc_en'][j]), dest=language_codes[i]).text
    else:
      ages_df.at[j, 'name'] = translator.translate(str(ages_df['en'][j]), dest=language_codes[i]).text
      ages_df.at[j, 'slug'] = ages_df.at[j,'slug_en'] + '-'+language_codes[i]
      ages_df.at[j, 'desc'] = translator.translate(str(ages_df['desc_en'][j]), dest=language_codes[i]).text

  print(ages_df)
  ages_df.to_csv('age-headings-'+language_codes[i]+'.csv', index=False,encoding='utf-8-sig')
