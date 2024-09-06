#!/bin/bash
cd arizona_edu
scrapy crawl arizona
mv data/* ../rawdata/
echo "Crawl completed and scraping data moved to rawdata"
