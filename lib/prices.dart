import 'package:flutter/material.dart';

class Prices extends StatefulWidget {
  const Prices({super.key});

  @override
  State<Prices> createState() => _Prices();
}

class _Prices extends State<Prices> {

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: const Color(0xFF0A0B2E),
        appBar: null,
        body: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: <Widget>[
            const SizedBox(height: 100),
            Row(
              children: [
                const Padding(
                  padding: EdgeInsets.only(top: 0, left: 110),
                  child: Text(
                    'Inflator Raider',
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      fontSize: 30,
                      fontFamily: 'Helvetica',
                      fontWeight: FontWeight.bold,
                      color: Colors.white,
                    ),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.only(left: 30),
                    child: SizedBox(
                        width: 35,
                        height: 35,

                        child: Stack(
                            children: <Widget>[
                              Positioned(
                                  top: 0,
                                  left: 0,
                                  child: Container(
                                      width: 35,
                                      height: 35,
                                      decoration: const BoxDecoration(
                                        color : Color.fromRGBO(76, 192, 129, 1),
                                        borderRadius : BorderRadius.all(Radius.elliptical(35, 35)),
                                      )
                                  )
                              ),Positioned(
                                  top: 5,
                                  left: 4,
                                  child: Container(
                                      width: 25,
                                      height: 25,
                                      decoration: const BoxDecoration(
                                        image : DecorationImage(
                                            image: AssetImage('assets/SettingsIcon.png'),
                                            fit: BoxFit.fitWidth
                                        ),
                                      )
                                  )
                              ),
                            ]
                        )
                    )
                )
              ]
            ),
            Column(
              children: [
                Padding(
                  padding: const EdgeInsets.only(top:10),
                  child: SizedBox(
                    width: 350,
                    height: 60,
                    child: Container(
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        color: const Color(0xFF101249),
                        borderRadius: BorderRadius.circular(30),
                      ),
                      child: const TextField(
                        decoration: InputDecoration.collapsed(
                          hintText: 'Search Item',
                          hintStyle: TextStyle(
                            fontSize: 24,
                            fontWeight: FontWeight.bold,
                            color: Colors.grey,
                          ),
                        ),
                        style: TextStyle(
                          fontSize: 24,
                          fontWeight: FontWeight.bold,
                          color: Colors.white,
                        ),
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
