import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

#creating a spark session.
from pyspark.sql import *
from pyspark.sql.functions import *
spark = SparkSession.builder.master('local[*]').appName('csvtoParquet').getOrCreate()

datasource0 = glueContext.create_dynamic_frame.from_catalog(database = " ", table_name = "", transformation_ctx = "datasource0")



#converting a glue catalog table into spark DataFrame.

df = datasource0.toDF()

df.write.format("parquet").save('s3://destination-bucket-name/file-name.parquet')
