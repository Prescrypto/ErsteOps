var socket_data = {};
$(function() {
  // Correctly decide between ws:// and wss://
  var ws_scheme = window.location.protocol == 'https:' ? 'wss' : 'ws';
  var ws_path =
    ws_scheme + '://' + window.location.host + '/ws//notify/emergency/';
  console.log('Connecting to ' + ws_path);
  var socket = new ReconnectingWebSocket(ws_path);

  // Helpful debugging
  socket.onopen = function() {
    console.log('Connected to notifications socket via dashboard.js');
  };
  socket.onclose = function() {
    console.log('Disconnected from notifications socket via dashboard.js');
  };

  socket.onmessage = function(message) {
    var dataTemp = JSON.parse(message.data);
    var data = JSON.parse(dataTemp);
    socket_data = data;
    console.log(socket_data);
    /*
        var notifications = $("#notifications")
        var ele = $('<tr></tr>')

        console.log(data);

        ele.append(
            $("<td></td>").text(data.type_notif)
        )
        ele.append(
            $("<td></td>").text(data.type_data)
        )
        ele.append(
            $("<td></td>").text(data)
        )

        notifications.append(ele)
        */
  };
});
