from aeneas.executetask import ExecuteTask
from aeneas.task import Task

#configurations for task
config_string = u"task_language=eng|is_text_type=plain|os_task_file_format=json"
task = Task(config_string=config_string)
task.audio_file_path_absolute = u"./music/rapgod.mp3"
task.text_file_path_absolute = u"./lyrics/aeneas_test_task.txt"
task.sync_map_file_path_absolute = u"./output/rapgod.json"

# process Task
ExecuteTask(task).execute()

# output sync map to file
task.output_sync_map_file()
