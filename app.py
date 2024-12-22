import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')
données['CA'] = données['qte'] * données['prix']

figure = px.pie(données, names='CA', title='CA total')
figure.write_html('CA-total.html')

print('CA-total.html généré avec succès !')
