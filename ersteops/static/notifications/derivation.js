$(function() {
  // Correctly decide between ws:// and wss://
  var ws_scheme = window.location.protocol == 'https:' ? 'wss' : 'ws';
  var ws_path =
    ws_scheme + '://' + window.location.host + '/ws/notify/derivation/';
  console.log('Connecting to ' + ws_path);
  var socket = new ReconnectingWebSocket(ws_path);

  // Helpful debugging
  socket.onopen = function() {
    console.log('Connected to notifications socket via derivation.js');
  };
  socket.onclose = function() {
    console.log('Disconnected from notifications socket via derivation.js');
  };

  socket.onmessage = function(message) {
    var dataTemp = JSON.parse(message.data);
    var data = JSON.parse(dataTemp);
    var notifications = $('#notifications');
    var ele = $('<tr></tr>');

    console.log(data);

    ele.append($('<td></td>').text(data.emergency));
    ele.append($('<td></td>').text(data.motive));
    ele.append($('<td></td>').text(data.hospital));
    ele.append($('<td></td>').text(data.eventualities));
    ele.append($('<td></td>').text(data.reception));
    ele.append($('<td></td>').text(data.notes));
    ele.append($('<td></td>').text(data.created_at));
    ele.append($('<td></td>').text(data.last_modified));

    notifications.append(ele);
  };
});
