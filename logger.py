import logging

def get_logger():
    """Configures and returns a logger for student processing."""
    logger = logging.getLogger("StudentProcessorLogger")
    
    if not logger.handlers:
        logger.setLevel(logging.ERROR)
        
        # Create file handler which logs even debug messages
        fh = logging.FileHandler('student_processor.log')
        fh.setLevel(logging.ERROR)
        
        # Create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        
        # Create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        
        # Add the handlers to the logger
        logger.addHandler(fh)
        logger.addHandler(ch)
        
    return logger
