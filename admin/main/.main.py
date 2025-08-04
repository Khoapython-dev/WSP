from lib.plugin.manager_plugin import get_key as plua
import json, os, time, random


plua.api("3c4f8b2d-5e3a-4b1c-9f0d-8e2f6b7c8d9e") # Agree Total Plugin
plua.delay(5)  # Delay for 5 seconds
plua.plugin_start("true")
plua.output("True")  # Output data if available
