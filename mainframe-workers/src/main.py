from message_queue.consumers.copybook_ibm_parser_consumer import CopybookIBMParserConsumer
import multiprocessing
import structlog

logger = structlog.get_logger()

def run_consumer(consumer_class):
    try:
        consumer = consumer_class()
        consumer.start_consuming()
    except Exception as e:
        logger.error(f"Error in {consumer_class.__name__}", error=str(e))
        raise

def main():
    consumers = [
        CopybookIBMParserConsumer
    ]
    
    processes = []
    
    try:
        for consumer_class in consumers:
            process = multiprocessing.Process(
                target=run_consumer,
                args=(consumer_class,)
            )
            processes.append(process)
            process.start()
            
        # Wait for all processes to complete
        for process in processes:
            process.join()
            
    except KeyboardInterrupt:
        logger.info("Shutting down consumers...")
        for process in processes:
            process.terminate()
            process.join()
    except Exception as e:
        logger.error("Application error", error=str(e))
        raise

if __name__ == "__main__":
    main() 