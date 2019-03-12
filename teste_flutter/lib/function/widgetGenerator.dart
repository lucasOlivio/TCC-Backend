import "package:flutter/material.dart";

void buildAlert(context,title,msg){ //Exibe modal na tela
  showDialog(
    context: context,
    builder: (BuildContext context) {
      return AlertDialog(
        title: new Text(title),
        content: new Text(msg),
        actions: <Widget>[
          new FlatButton(
            child: new Text("Fechar"),
            onPressed: () {
              Navigator.of(context).pop();
            },
          ),
        ],
      );
    },
  );
}