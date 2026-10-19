from comum import criar_sessao, exigir_camada, glob_eventos, gravar_eventos, ler_eventos, titulo
from pyspark.sql.types import (
    ArrayType, BooleanType, DoubleType, LongType,
    StringType, StructField, StructType, MapType
)
import pyspark.sql.functions as F

SCHEMA = StructType([
    StructField("event_id", StringType(), True),
    StructField("event_name", StringType(), True),
    StructField("event_ts", StringType(), True),
    StructField("user_pseudo_id", StringType(), True),
    StructField("user_id", StringType(), True),
    StructField("session_hint", StringType(), True),
    StructField("page", StructType([
        StructField("location", StringType(), True),
        StructField("referrer", StringType(), True)
    ]), True),
    StructField("traffic", StructType([
        StructField("source", StringType(), True),
        StructField("medium", StringType(), True),
        StructField("campaign", StringType(), True)
    ]), True),
    StructField("device", StructType([
        StructField("category", StringType(), True),
        StructField("os", StringType(), True),
        StructField("browser", StringType(), True)
    ]), True),
    StructField("items", ArrayType(StructType([
        StructField("item_id", StringType(), True),
        StructField("item_name", StringType(), True),
        StructField("item_category", StringType(), True),
        StructField("price", DoubleType(), True),
        StructField("quantity", LongType(), True)
    ])), True),
    StructField("params", MapType(StringType(), StringType()), True)
])

spark = criar_sessao("bronze")
exigir_camada(spark, glob_eventos("landing"), "python gerador/gerar_eventos.py")
landing = ler_eventos(spark, "landing", "json", schema=SCHEMA)
bronze = (
    landing
    .withColumn("_arquivo_origem", F.input_file_name())
    .withColumn("_ingestao_ts", F.current_timestamp())
)
gravar_eventos(bronze, "bronze", "append")
titulo("Bronze")
spark.stop()
