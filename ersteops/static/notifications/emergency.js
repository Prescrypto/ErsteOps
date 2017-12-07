
$(function () {
    // Correctly decide between ws:// and wss://
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var ws_path = ws_scheme + '://' + window.location.host +  "/notify/emergency/";
    console.log("Connecting to " + ws_path);
    var socket = new ReconnectingWebSocket(ws_path);

    // Helpful debugging
    socket.onopen = function () {
        console.log("Connected to notifications socket");
    };
    socket.onclose = function () {
        console.log("Disconnected from notifications socket");
    };

    socket.onmessage = function(message) {
        var dataTemp = JSON.parse(message.data);
        var data = JSON.parse(dataTemp);
        var notifications = $("#notifications")
        var ele = $('<tr></tr>')

        ele.append(
            $("<td></td>").text(data.odoo_client)
        )
        ele.append(
            $("<td></td>").text(data.grade_type)
        )
        ele.append(
            $("<td></td>").text(data.zone)
        )
        ele.append(
            $("<td></td>").text(data.start_time)
        )
        ele.append(
            $("<td></td>").text(data.end_time)
        )
        ele.append(
            $("<td></td>").text(data.is_active)
        )
        ele.append(
            $("<td></td>").text(data.unit)
        )
        ele.append(
            $("<td></td>").text(data.created_at)
        )
        ele.append(
            $("<td></td>").text(data.last_modified)
        )
        
        notifications.append(ele)
    };

});