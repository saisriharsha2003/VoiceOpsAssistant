import speedtest
from virtual_assistant import speak, inputCommand, desktop_assistant

def check_network_speed():
    st = speedtest.Speedtest()
    print(desktop_assistant+": Loading server list...")
    speak("Loading server list...")
    st.get_servers()
    print(desktop_assistant+": Choosing best server...")
    speak("Choosing best server...")
    best = st.get_best_server()
    print(f"{desktop_assistant}: Found {best['host']} located in {best['country']}")
    speak(f"Found: {best['host']} located in {best['country']}")
    print(desktop_assistant+": Performing download test...")
    speak("Performing download test...")
    download_speed = st.download() / ((10 ** 6)*8)
    print(desktop_assistant + f": Download Speed is: {download_speed:.2f} MBbps")
    speak(f"Download Speed is: {download_speed:.2f} MBps")
    print(desktop_assistant+": Performing upload test...")
    speak("Performing upload test...")
    upload_speed = st.upload() / ((10 ** 6)*8)
    print(desktop_assistant + f": Upload Speed is: {upload_speed:.2f} MBps")
    speak(f"Upload Speed is: {upload_speed:.2f} MBps")
    ping_result = st.results.ping
    print(f"{desktop_assistant}: Ping {ping_result}ms")
    speak(f"Ping: {ping_result}ms")