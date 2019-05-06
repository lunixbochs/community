from talon import speech_system
import logging

def debug(topic, j):
    logging.info(f"[speech_system] {topic} {j}")

speech_system.register('', debug)
