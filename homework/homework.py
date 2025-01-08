"""
Escriba el codigo que ejecute la accion solicitada.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import zipfile as zp

#Cliente

listcv = []
for a in range(10):
    path = "files/input/bank-marketing-campaing-" + str(a) + ".csv.zip"
    archivo = zp.ZipFile(path, "r")
    pathotro = "bank_marketing_" + str(a) + ".csv"
    csv =  archivo.open(pathotro)
    name = "csv" + str(a)
    listcv.append(pd.read_csv(csv))


df_concatenado = pd.concat(listcv, ignore_index=True)
#print(df_concatenado.columns)
client = df_concatenado[["client_id", "age", "job", "marital", "education", "credit_default", "mortgage"]]
client["job"] = client["job"].str.replace(".", "").str.replace("-", "_")
client["education"] = client["education"].str.replace(".", "_").str.replace("unknown", "<NA>")
client["credit_default"] = client["credit_default"].str.replace("unknown", "0").str.replace("yes", "1").str.replace("no", "0")
client["mortgage"] = client["mortgage"].str.replace("unknown", "0").str.replace("yes", "1").str.replace("no", "0")
#print(client)

client.to_csv("files/output/client.csv", index=False)

#Campaign
#print(df_concatenado.columns)
campana = df_concatenado[["client_id", "number_contacts", "contact_duration", "previous_campaign_contacts", "previous_outcome", "campaign_outcome"]]
campana["previous_outcome"]  = campana["previous_outcome"].str.replace("unknown", "0").str.replace("success", "1").str.replace("nonexistent", "0").str.replace("failure", "0")
campana["campaign_outcome"]  = campana["campaign_outcome"].str.replace("unknown", "0").str.replace("yes", "1").str.replace("no", "0")
campana["last_contact_date"] = pd.to_datetime("2022-" + df_concatenado["month"].astype(str) + "-" + df_concatenado["day"].astype(str),format="%Y-%b-%d" )

campana.to_csv("files/output/campaign.csv", index=False)

#economics

economics =df_concatenado[["client_id", "cons_price_idx", "euribor_three_months"]]
economics.to_csv("files/output/economics.csv", index=False)

print(campana.columns)
def clean_campaign_data():
    """

    client.csv:
    - client_id
    - age
    - job: se debe cambiar el "." por "" y el "-" por "_"
    - marital
    - education: se debe cambiar "." por "_" y "unknown" por pd.NA
    - credit_default: convertir a "yes" a 1 y cualquier otro valor a 0
    - mortage: convertir a "yes" a 1 y cualquier otro valor a 0

    campaign.csv:
    - client_id
    - number_contacts
    - contact_duration
    - previous_campaing_contacts
    - previous_outcome: cmabiar "success" por 1, y cualquier otro valor a 0
    - campaign_outcome: cambiar "yes" por 1 y cualquier otro valor a 0
    - last_contact_day: crear un valor con el formato "YYYY-MM-DD",
        combinando los campos "day" y "month" con el año 2022.

    economics.csv:
    - client_id
    - const_price_idx
    - eurobor_three_months



    """

    return


if __name__ == "__main__":
    clean_campaign_data()
