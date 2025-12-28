import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s"
)

logger = logging.getLogger("ai-12weeks")

def main():
    logger.info("Logging initialized")
    logger.warning("Sample warning")

if __name__ == "__main__":
    main()