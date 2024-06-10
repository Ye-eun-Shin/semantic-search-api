import os
import json

import numpy as np


def normalize(sent: str):
    """Normalize sentence"""
    sent = sent.replace("“", '"')
    sent = sent.replace("”", '"')
    sent = sent.replace("’", "'")
    sent = sent.replace("‘", "'")
    sent = sent.replace("—", "-")
    sent = sent.replace("_", " ")
    return sent.replace("\n", "")


def load_dataset(f_input: str):
    """Load dataset from input directory"""
    with open(f"{f_input}.json", "r", encoding="utf-8") as corpus:
        lines = [normalize(line["content"]) for line in json.loads(corpus.read())]
        return lines


def es_search(es, index: str, query: str, k: int = 3):
    """Conduct ElasticSearch's search"""
    results = es.search(
        index=index, body={"from": 0, "size": k, "query": {"match": {"content": query}}}
    )
    results = [result["_source"]["content"] for result in results["hits"]["hits"]]
    return results


def create_es_index(es, index: str):
    """Create ElasticSearch indices"""
    if not es.indices.exists(index=index):
        es.indices.create(
            index=index,
            body={
                "settings": {
                    "analysis": {"analyzer": {"nori": {"tokenizer": "nori_tokenizer"}}}
                },
                "mappings": {
                    "properties": {"content": {"type": "text", "analyzer": "nori"}}
                },
            },
        )

        dataset = load_dataset(index)

        for data in dataset:
            doc = {"content": normalize(data)}
            es.index(index=index, body=doc)

