'''*************/
/* CatPlay     */
/* Version 1.0 */
/* Jigar Hira  */
/* June 2019   */
/*************'''


import socket


PACKETSIZE = 1024


# Starts the web socket for video
def socket_start():
    video_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    video_socket.bind('localhost', '1234')
    video_socket.listen()
    return video_socket


# Sends data packet to socket
def socket_send(socket, input_stream):
    # Waits for client request
    client, address = socket.accept()
    print(f"Connection from {address} has been established.")









# Unit test
if __name__ == '__main__':
    start_socket()

# EOF