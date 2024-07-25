 import pandas as pd
import matplotlib.pyplot as plt

def plot_spectrum(csv_file):
    # Carregar dados do arquivo CSV
    df = pd.read_csv(csv_file, names=['Frequency', 'Amplitude'])

    # Plotar espectro
    plt.figure(figsize=(12, 6))
    plt.plot(df['Frequency'], df['Amplitude'], color='blue')
    plt.title('Spectrum Analyzer')
    plt.xlabel('Frequency (MHz)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    csv_file = 'output.csv'  # Nome do arquivo CSV gerado pelo rtl_power
    plot_spectrum(csv_file)
