# GoalKicker.com – Python® Notes for Professionals 394

if __name__ == '__main__':
    try:
        import requests
    except ImportError:
        print("To use this module you need 'requests' module")
        t = input('Install requests? y/n: ')
        if t == 'y':
            from pip._internal import main, pip

            t = input(pip.__version__)
            main(['install', 'requests'])
            t = input('Installed requests ')
            import requests

            t = input(requests.__version__)
            import os
            import sys

            pass
        else:
            import os
            import sys

            print('Some functionality can be unavailable.')
else:
    import requests
    import os
    import sys
