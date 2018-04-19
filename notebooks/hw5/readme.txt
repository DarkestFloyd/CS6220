Create index in Kibana:
1. 20ng 
  a. Data
    PUT /20ng
    {
     "mappings": {
      "doc": {
       "properties": {
        "doc_id": {"type": "keyword"},
        "doc_text": {"type": "text"}
       }
      }
     }
    }

  b. Topics
    PUT /topics20ng
    {
      "mappings": {
        "topic": {
          "properties": {
            "topic_id": { "type": "integer"},
            "top_words": { "type": "text"},
            "word_prob": {"type": "text"}
          }
        }
      }
    }

2. DUC
  a. Data
    PUT /duc
    {
     "mappings": {
      "doc": {
       "properties": {
        "doc_id": {"type": "keyword"},
        "doc_text": {"type": "text"},
        "gold_summary": {"type": "text"}
       }
      }
     }
    }

  b. Topics
    PUT /topicsduc
    {
      "mappings": {
        "topic": {
          "properties": {
            "topic_id": { "type": "integer" },
            "top_words": { "type": "text" },
            "word_prob": { "type": "text" }
          }
        }
      }
    }
