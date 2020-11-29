# SF Crime Statistics with Spark Streaming

## Screenshots
Please see screenshots.pdf


## Question 1: How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
Increasing of maxOffsetsPerTrigger increases throughput (processedRowsPerSecond), but you have to be careful because latency also gets increased as it takes more time to complete the batch.

## Question 2: What were the 2-3 most efficient SparkSession property key/vlues pairs?
Regarding the sample data, the dataset size is so small, that the default size for memory options (spark.driver.memory, spark.executor memory) is satisfying --> so changing this values did not make sense in this case.

I played around with setting   maxRatePerPartition and spark.straming.kafka.maxRatePerPartition, but that did not really make a difference when looking at the resulting progress reporters. I guess that was because of the local setting in the provided workspace.
