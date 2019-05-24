from ps6 import *


story = get_story_string()


a = CiphertextMessage(story)
print(a.decrypt_message())