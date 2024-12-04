#!/usr/bin/env python3
import os, sys

from proj.parser import get_parser
from proj.logger import get_root_logger, ROOT_LOGGER_NAME

def main():    
    parser = get_parser()
    args = parser.parse_args()
    logger = get_root_logger(ROOT_LOGGER_NAME, args.log_level, args.verbose)
    logger.info("Starting proj...")
    
if __name__ == "__main__":
    main()