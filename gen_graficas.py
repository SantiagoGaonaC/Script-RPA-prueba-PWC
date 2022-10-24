import matplotlib.pyplot as plt

def gen_graficos(df):
    
    plt.subplots(num="Gráficos")
    
    #Países donde más se compra
    plt.subplot(221)
    df['País'].value_counts().plot(kind="bar", title="Países que más compran",
                                   ylabel="Cantidad")
    plt.legend()
    
    #Envios locales y internacionales
    plt.subplot(222)  
    explode = (0.3,0)
    df_envio = df['Envio'].value_counts()
    df['Envio'].value_counts().plot(kind="pie", 
                                    title="Números de envios",
                                    explode=explode, 
                                    autopct=lambda p: '{:.2f}%({:.0f})'.format(p,(p/100)*df_envio.sum()),
                                    shadow=True)
    plt.legend()
    
    #Cantidad de correos validos o no validos
    plt.subplot(223)
    df_valido = df['Correo_Valido'].value_counts()
    df['Correo_Valido'].value_counts().plot(kind="pie", title="Correos validos",
                                   ylabel="Cantidad",
                                   autopct=lambda p: '{:.2f}%({:.0f})'.format(p,(p/100)*df_valido.sum()),
                                   figsize=(13,13))
    plt.legend()
    
    #Marcas que más venden
    plt.subplot(224)
    df['Marca'].value_counts().plot(kind="bar", title="Marcas que más venden",
                                   ylabel="Cantidad")
    plt.legend()

    #--------------------
    #tamaños automaticos
    plt.tight_layout()
    #mostar PLT  
    plt.savefig("Gráficos.pdf")
    plt.clf()
    #-------------------