import asyncio

from aioconsole import ainput

class Console:
    def __init__(self, switch):
        self.switch = switch
        self._console = ainput
        self.__running = False

    def __execute(self, command):
        if command == 'boot':
            self.switch.boot()
        elif command == 'run':
            self.switch.run()
        elif command == 'stop':
            self.switch.stop()
        elif command == 'shutdown':
            self.switch.shutdown()
        elif command == 'interfaces':
            print(self.switch.interface_manager.return_json())
        elif command.startswith('input interface:'):
            inter_name = command.split(' ')[-1].strip()
            self.switch.choose_inter_to_run(inter_name)
        elif command.startswith('delete interface:'):
            inter_name = command.split(' ')[-1].strip()
            self.switch.delete_inter_to_run(inter_name)
        elif command == 'show macs':
            self.switch.mac_table.return_json()
        elif command == 'help':
            print('boot - boot switch')
            print('run - run switch')
            print('stop - stop switch')
            print('shutdown - shutdown switch')
            print('interfaces - show interfaces')
            print('input interface: <interface name> - input interface to run')
            print('delete interface: <interface name> - delete interface from running')
            print('show macs - show mac table')
            print('help - show help')
            print('exit - exit from console')
        elif command == 'exit':
            try:
                self.switch.stop()
                self.switch.shutdown()
            except:
                pass
            finally:
                self.shutdown()
        else:
            print('Unknown command')

    def boot(self):
        self.__running = True
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.__start(loop))

    async def __start(self, loop):
        while self.__running:
            command = await self._console('>>> ')
            try:
                await loop.run_in_executor(None, self.__execute, command)
            except Exception as e:
                print(e)

    def shutdown(self):
        print('Console is shutdown')
        self.__running = False
