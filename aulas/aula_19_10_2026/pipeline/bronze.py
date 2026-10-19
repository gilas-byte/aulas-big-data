from comum import criar_sessao, exigir_camada, glob_eventos, gravar_eventos, ler_eventos, titulo

SCHEMA = ...   # o schema explícito da landing (R4): escreva o seu

spark = criar_sessao("bronze")
exigir_camada(spark, glob_eventos("landing"), "python gerador/gerar_eventos.py")
landing = ler_eventos(spark, "landing", "json", schema=SCHEMA)
bronze = ...   # proveniência e partições year/month/day (R4): é aqui que está o seu trabalho
gravar_eventos(bronze, "bronze", "append")
titulo("Bronze")
spark.stop()
