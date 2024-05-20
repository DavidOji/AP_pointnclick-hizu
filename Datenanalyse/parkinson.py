import pandas as pd
import matplotlib.pyplot as plt

# Daten laden
data = pd.read_csv('CSV/parkinsons+telemonitoring/parkinsons_updrs.data')

# Erkunden des DataFrames
print("Erste 5 Zeilen:")
print(data.head())
print("\nLetzte 5 Zeilen:")
print(data.tail())
print("\nDimensionen des DataFrames:")
print(f"Anzahl der Zeilen: {data.shape[0]}, Anzahl der Spalten: {data.shape[1]}")
print("\nDatentypen der Spalten:")
print(data.dtypes)

# Datenbereinigung
print("\nFehlende Werte pro Spalte vor der Bereinigung:")
print(data.isnull().sum())
data.dropna(inplace=True)  # Fehlende Werte entfernen
data.drop_duplicates(inplace=True)  # Duplikate entfernen

# Überprüfen und Konvertieren der Datentypen
# Schleife über alle Spalten, um nötige Konvertierungen durchzuführen
for column in data.columns:
    if data[column].dtype == 'object':
        # Versuch, die Spalte in einen numerischen Typ zu konvertieren, falls sie als 'object' gekennzeichnet ist
        try:
            data[column] = pd.to_numeric(data[column], errors='coerce')
        except ValueError:
            # Wenn die Konvertierung fehlschlägt, handle die Spalte als kategorisch
            data[column] = pd.Categorical(data[column])

print("\nDatentypen nach Überprüfung und Konversion:")
print(data.dtypes)

# Datenanalyse
print("\nDeskriptive Statistiken für jede numerische Spalte:")
print(data.describe())
correlation = data.corr(numeric_only=True)
print("\nKorrelationen in den Daten:")
print(correlation)

# Datenvisualisierung
data['total_UPDRS'].hist()
plt.title('Verteilung von total_UPDRS')
plt.show()

plt.scatter(data['motor_UPDRS'], data['total_UPDRS'])
plt.title('Motor UPDRS vs. Total UPDRS')
plt.show()

data.boxplot(column='total_UPDRS', by='age')
plt.title('Total UPDRS nach Alter')
plt.show()
