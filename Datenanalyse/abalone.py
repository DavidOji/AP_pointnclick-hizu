import pandas as pd
import matplotlib.pyplot as plt

# Daten einlesen
# Definieren der Spaltennamen, um sie während des Ladevorgangs den Daten zuzuordnen
column_names = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']
# Laden der Daten aus einer CSV-Datei. Da die Originaldatei keine Kopfzeile hat, wird 'header=None' verwendet und 'names' gibt die Spaltennamen an.
data = pd.read_csv('CSV/abalone/abalone.data', header=None, names=column_names)

# Erkunden der geladenen Daten
# Ausgabe der ersten 5 Zeilen, um einen ersten Eindruck von den Daten zu bekommen
print("Erste 5 Zeilen des DataFrames anzeigen:")
print(data.head())
# Ausgabe der letzten 5 Zeilen, um zu sehen, wie die Daten am Ende der Datei aussehen
print("\nLetzte 5 Zeilen des DataFrames anzeigen:")
print(data.tail())
# Überprüfen der Dimension des DataFrames, einschließlich der Anzahl der Zeilen und Spalten
print("\nDimensionen des DataFrames überprüfen (Zeilen und Spalten):")
print(f"Anzahl der Zeilen: {data.shape[0]}, Anzahl der Spalten: {data.shape[1]}")
# Überprüfung der Datentypen der Spalten, um die korrekte Behandlung der Daten zu gewährleisten
print("\nDatentypen der Spalten überprüfen:")
print(data.dtypes)

# Datenbereinigung
# Ausgabe der Summe fehlender Werte pro Spalte, um festzustellen, ob und wo es Datenlücken gibt
print("\nFehlende Werte pro Spalte vor der Bereinigung anzeigen:")
print(data.isnull().sum())
# Entfernen von Zeilen mit fehlenden Daten, falls vorhanden
data.dropna(inplace=True)
# Entfernen von Duplikatzeilen, um die Genauigkeit der Analyse zu erhöhen
data.drop_duplicates(inplace=True)

# Überprüfen und Konvertieren der Datentypen
# Schleife über alle Spalten, um nötige Konvertierungen durchzuführen
for column in data.columns:
    if column == 'Sex':
        # Konvertieren der 'Sex'-Spalte in einen kategorischen Datentyp für eine effizientere Speicherung und Verarbeitung
        data['Sex'] = pd.Categorical(data['Sex'])
    elif data[column].dtype == 'object':
        # Versuch, die Spalte in einen numerischen Typ zu konvertieren, falls sie als 'object' gekennzeichnet ist
        data[column] = pd.to_numeric(data[column], errors='coerce')

# Nach Überprüfung und Konvertierung die Datentypen erneut ausgeben
print("\nDatentypen nach Überprüfung und Konversion:")
print(data.dtypes)

# Datenanalyse
# Deskriptive Statistiken für jede numerische Spalte ausgeben, um zentrale Tendenzen und Streuungen zu verstehen
print("\nDeskriptive Statistiken für jede numerische Spalte:")
print(data.describe())
# Berechnen der Korrelation zwischen 'Rings' und anderen Eigenschaften, um Zusammenhänge aufzudecken
correlation = data.corr(numeric_only=True)
print("\nKorrelation der 'Rings' mit anderen Eigenschaften (zeigen den Zusammenhang auf):")
print(correlation['Rings'].sort_values())

# Datenvisualisierung
# Histogramm für die Länge erstellen, um die Verteilung visuell zu analysieren
data['Length'].hist()
plt.title('Verteilung der Länge')
plt.show()

# Scatter Plot erstellen, um die Beziehung zwischen Länge und Anzahl der Ringe zu visualisieren
plt.scatter(data['Length'], data['Rings'])
plt.title('Länge vs. Ringe')
plt.show()

# Boxplot erstellen, um die Verteilung der Ringe basierend auf dem Geschlecht zu untersuchen
data.boxplot(column='Rings', by='Sex')
plt.title('Ringe nach Geschlecht')
plt.show()
