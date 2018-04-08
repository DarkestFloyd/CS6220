Create index in Kibana:
1. 20ng 
    PUT /20ng
    {
     "mappings": {
      "doc": {
       "properties": {
        "doc_id": {"type": "keyword"},
        "doc_text": {"type": "keyword"}
       }
      }
     }
    }

2. DUC
    PUT /duc
    {
     "mappings": {
      "doc": {
       "properties": {
        "doc_id": {"type": "keyword"},
        "doc_text": {"type": "keyword"},
        "gold_summary": {"type": "keyword"}
       }
      }
     }
    }
