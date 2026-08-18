from client import ConversationalPersonalMemoryTimelineExtractorClient

def main():
    client = ConversationalPersonalMemoryTimelineExtractorClient()
    stream = "Need to review the Series A term sheet with legal counsel before Thursday afternoon."
    res = client.process_memory_stream(stream)
    print(f"Event Created: {res['timeline_event_created']}")
    print("Tasks Extracted:", res["extracted_tasks"])
    print("Entities:", res["semantic_entities"])

if __name__ == "__main__":
    main()
