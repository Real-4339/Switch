# This file contain perspective 'good' ides that i want to implement in the project.

- Add to footer a console output of the program, like this:
```
[2021-10-13 16:00:00,000] [INFO] [app.py] [main] [line: 1] [thread: 1] [pid: 1] [message: 'Program started']
```

The idea is when running program from pc console it locks console, so i want to create background subprocess and put every output from program to website so user also see whats going on in the program. That console will be placed in the footer of the program. The console will aslo take commands such as `clear` and `exit` in the console. `clear` will clear the console and `exit` will exit the program and end subprocess.
