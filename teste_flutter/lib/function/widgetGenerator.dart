import "package:flutter/material.dart";

void buildAlert(context,title,msg){ //Exibe modal na tela
  showDialog(
    context: context,
    builder: (BuildContext context) {
      return AlertDialog(
        title: Text(title),
        content: Text(msg),
        actions: <Widget>[
          FlatButton(
            child: Text("Fechar"),
            onPressed: () {
              Navigator.of(context).pop();
            },
          ),
        ],
      );
    },
  );
}