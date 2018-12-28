# Asciify
Converts your images into ASCII art.
Comes with the following implementations:
* Local files
* Flask endpoint for POST requests (image should be in base64 string format)
* Discord bot

## Prerequisites
* Python 3.5+ (which introduced `async/await` coroutines)
* Pip

## Setting Up
* Install required python packages
```
pip install -r requirements.txt
```

#### Flask
No setup required.

#### Discord
* Create a Discord bot account. Instructions: https://discordpy.readthedocs.io/en/rewrite/discord.html
* Replace the values in `config.py` with your own information from following the instructions in the link above

```
"DISCORD": {
    "APP_CLIENT_ID": <your_app_client_id>,
    "APP_CLIENT_SECRET": "<your_app_client_secret>",
    "BOT_TOKEN": "<your_bot_token>",
    "SERVER_ID": your_server_id
}
```

## Usage

#### Local Files
`python3 local_file.py /path/to/image/ width height`
   
   ![local_file_result](./resources/local_file_result.png)

#### Flask

* Run the Flask application
```
export FLASK_APP=flask_endpoint.py
flask run
```

* Send a POST request to the server (default is `http://127.0.0.1:5000`) with the following as a JSON payload
```
{
    "image": "<your image in base64 string>"
    "width": <desired width of ascii result>,
    "height": <desired height of ascii result>,
}
```

* Example:

```
Request:
 
{
    "image": "iVBORw0KGgoAAAANSUhEUgAAAgAAAAIACAYAAAD0eNT6AAAACXBIWXMAANHsAADR7AH41yZLAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAIABJREFUeNrtnQeYVdXVvycxRmNJjKYqMIXey9B7n3LuGUEdjUZNYgyIQbF3DXaxMIUmHUFFEBAp0qRKmblzQfEL0b/EWGI0VpgCM7RZ/7PPYGKUMjPce885e7+/53kfk3x+MHPWPvu3zt5rr52QgBAKlGRH9hkSPr+uRDJbylarh4RDthTZV0hRaLhErNsd7nf++2POf58gRdYU5z/P/Q/h0GLnf191RNz/2//8u5Or/gznz1J/pvqz1d+h/i71d6q/W/0M6mdxfiYigxBCCNXG2DennS1bs1pJoR2SSOgax2QfPGzCi5x/bnH++b7DXgfxKXudJOG9wz/ry+7PHrYfcH8X93dykoU3rZ8SaYQQQqZ9uf9QCjMbOeaYKRH7eudLOt/5z684/M1hj4+NPdqUHf6dlzpJQp6TNFznPIsM99k4z4iRghBCKJhGv7b3qVKU1dYx+cucr99HHKN7yfnnO84/Dxpk8rXloPusIqEFTlLwsMOlEs5so54pIwshhJB/zD7S/yeO0Xd3vmRHOOY10/ma3YHRxygxKAq9e7iGYaRbg7B98C8YgQghhOLxZf8Dx+zbVS1Zh144vCePOXuLisFsNyYqNnOzT2KkIoQQOjHDV9X26uteVb9XfXnuwnCDUF9gbXRPLqhVAooOEUIIHdfwI3Y9xzR+6xj+OMdItrOUr01NwRvOP8e6NRkFGXUY6QghZLrhVy3pdz98Zj7iUIlhGsG7TswnuisEOzNO4U1ACCETTL/QTpYia0hVs5tQMWZoPHvcJkhuAyW7CW8IQgjp85V/qmP4/b/xlY/pQfVWBzh6iBBCATP9iH2ahO2LnYl8vmENdiD6qwPzJGJlqzHFm4UQQn790nd74odmOpRgXhD1NsdVJ0GulO0DT+eNQwghL01/Z8Yp3zB99vMh/skAKwMIIRQn04+kniwRy3Im32ekyN6NGYG3OGMwbM+out8h9WTeUIQQirbxF4QaHm7u8immAz7lK7eAsMhqwRuLEEInYvpqiV8VYFXdV88ZfQgSEfe4KVsECCFUk2V+u8nhY3ufYyQQcHa5qwKFoda82QghdCTTV1X8//3axzhA31WBHdln8MYjhDD+IivF+ULKp4ofzCocDOWprpTMAAghE5f52x0+vncAQwBDOeQeJwxbXZkREEJ6m76M/P7hc/ss8wN8Z3sgdKXMzT6JmQIhpI/xq2p+NbkVhf7GRA9wzO2BvztJ8ghODyCEgm382wf/wpnURlLND1BjPndPwmzLOpeZBCEUHOMPZ/5KIqFcZxIrZyIHOMG2w0XWaJVMM7MghPxr/IWDzzn8xc9lPADRpcw9OVCQ9UtmGoSQf4x/Y9aZErFupzc/QMwpdbcG3rR+ysyDEPLO+Hdkn1Fl/KoHOpMzQBwpcROBSP+fMBMhhOJn/BH7NLdSuSj0byZiAE/5wt1225h1JjMTQih2xr+29w+cyWY4xg/gOz6RiDVMvaPMVAih6Jp/ONRPiuw3mWgBfM1bznuawYyFEDpx4y8INXQmlLlMrACBYpVstZoygyGEam78qsCv6khfBZMpQCC7Cu53jw5SKIgQqpbxq379VW172ecH0KVQUBXtcs8AQuio5l8U6i2R0BtMmABask3CmT2Z6RBC/zV+1bqXfX4AMwiHnqO1MELGL/cnfO/wcv8XTIwARrFLiqwhag5gJkTIuOV+K8WtFGYiBDCZdVKY2YgZESETjF8186nq4lfG5AcA7o2DqqU3RYIIaWz+haHWzsseZsIDgCPwuhRmtmemREgn49+c/aOqM/32fiY5ADgGB9zeAdsHns7MiVDQzT+c2dMx/r8zsQFAtYmE3pGI3Z0ZFKGg7vVXdfI7yIQGALXgkLsasCP7h8yoCAVmr99Odl7eTUxgABAFwupOEGZWhPxu/lXn+kuZtAAgqicFwqERzLAI+dH4Xx90lvOSzmaiAoAYXjA0XwoHn8OMi5BfzD8c6ieR0EdMTgAQBz6RcGY6My9CXhp/JPXkw4V+h5iUACCOVLoFgjszTmEmRiju5p9R323cwUQEAN4RkS2DkpiREYqX+RfZGc6L9xWTDwD4gC9lq5XGzIxQLI1f3d6nenaz5A8AftsSKLIfExn5fWZqhKJt/gUZP5ZIaAETDQD4+JTAEnUiiRkboajt99tNnJfrLSYXAAgAOyWS2ZKZG6ET3++/VLi6FwCCRamEQ5cwgyNUG+N3e/nbjzGRAECAtwQmquPKzOgIVX/J/2dO9ryByQMANGAt3QMRqpb5u+f732bSAACNVgL+LkVZjZnhETqa+W+1Ozsvy2dMFsdmz4YM+WhJf/nr872kYEo3eTW/kyx8NFWeva+1TLqlhYy7obmMvraJPHJ1Q3noqoYy8sr6ctelyf+D+t/U/02h/l31/zPjzlYy98G2svTJDrJuXGeJTO8ub73QSz5c1E92r0nn2QOceL+AHsz0CH2n2C90kXvjFpOEHCq05NPlA+TN53rKytyOMuue1pIzvKncd0V9GW7XlT+lnecJ11p15S/OzzBmRDN5YWQbWe0kHttn9ZB/Le0vBwosJniA41OhCpuZ8RH62vzDoRGmNvdRX/Nvz+0tqxyjn3ZHS7n/dw1kWGYdz0y+tlyTeZ77s0+7s6Wsyuvk/k7qd2PCBzhS06DQSGZ+ZLbxz80+ScL2eFNe/MpwyP1aXj++i2v2d1+WEjijryl3/iZFJt7cQtaM6eRuW1SGWSkAqMKawgkBZKb578g+w+2apflL/vEr/dwv4jHXN5MbBtXT3vCPh3oGY0c0c7c23l/Yl4QATE8CVqoupzgCMsf8t2Wd6wz+bTq+0GXr06VwSjeZfkcrufWiJOMN/3jcdGGS+6xUwWH5RrYMwMgTAm9K+Py6OAPS3/wLMxs5g/5DnV7gL18dKKvzO8uTwxrL0PQ6GPsJ1BE8dW0T91TDrtVpGAOYxPuyNasBDoH0Nf+C85s5A/1fOrywX6wa4B6Xe+iqBjIkHfOONkOcROrJaxq7xxFL13MEEYzg39whgPQ0/61WqjPAPw/08v6GDFk/vrOMGtIY048jQzPquDUUr8/s7h6RxChAY75ykoBOOAbSx/wjdndnYBcH8kx+2JI3ZvWQcTc2D+TxPN24+cJEmf9wW/lsxUDMAnStCdgtRVndcA4UfPMvCvV2b8YK2Euo9qCXPN5ebr84GeP16RaB6l6oOhViGKAhe5wkYAAOggL85W9ZzkAuD9KL9zfHUCbc2MxddsZog8HDVzV0V2lUnwWMA7TqGhixB+EkKHjmH7YvliJ7f1BetvcW9pXHhzbCUAPMg79vKP9Y0BfjAJ044MyjV+AoKEDmH/pt1cANxku2fHQHivp0KRhMryMvPthODhZgHqANB6XIugpnQUEw/z8c7nUdiJdr9sg2GKeGqG0cLigCjTgkYfv3OAzysflbFwTpy/+1pztjljonATc1py4AdFsJ+A1Og3xo/pnpVVddBqeRj7reFqPUG9VICOMAjY4I7pdwyMZxkJ+W/fsFrdr/+b+w9G8Cw+26smsNbYVBK/apDy6cB3lv/oWhLkE751++KUP+HOLr3xTmPdQO0wD9+gSEM3viQMjLZf82buvKgL08f32+F8ZoECMG1ZP9WygIBO0olsLM9jgRir/5RzJbOgPwiyC+OAsfS8UYDeOdF/tgGKAjn0vYbo4jofiZf0GooRTZHwf1pXn23taYomG88lQHzAL0JBz6VCJ2E5wJxWHZ//y6zqD7MMgvzLQ7WmKKhvH8fW0wCtCZ92Vz6DwcCsXO/DdmnSmR0BtBf1nmPNAWUzSMGXe1wiRAd/5PIv1/glOhGOz5p57sDLAVOrwoOjUAutaqI/deXl8eH9rYvbJYGZ1qhbvsyQ6yYUIX2Tqju3vB0bfZOa+3vL+wr3sHgvrvkend3eeyKrejLBqV6iZJ0+9oJU8NayJ3X5bi/j2sAAD4vk/AMlnb+wc4Fory0r89XpeX5KMl/QNlXsMy68jIK+vL0zc3l5cfay/hqd3kHy/1leK18T3fvntNuvv3qmRBXZWsfp77rqgfiJsT142lIRAYUxMwGcdC0TP/Iusu3V6Sh65q4M/LbBwzVdfbPntfa3nN+YL/YFFf319sc2CL5f6cmyd1dQssVbIyJN1fSYFa6cAcwCBuxblQNL78L3YvotDsBVHL435Zwn9yWGNZNKq9vDWnl1RsytTi+ZZvzHD7LagVi0evbuTe0ufVM77v8gYYAphGpUTsy3AwdAL7/nb3oLX4rS6HCi25/3cNPDOkOfe3cQ1y3+ZMIyaksg0ZUjS9m1ujcPOFiXF93qvzWf4HIymXsNUVJ0O1MP+M+s4A+kznF+QfC/rKsDgUt6nl8FFDGsvK3I7y+coBxk9MlWHLbcwze2RrufWipJg++4euauj7LRSAGPKFFGY2wtFQ9c2/cPA5Egm9Y8ILsmVKN8egY2H657mmr4rPitemMxEdIxlQpxAm3dIi6snY8Kx68vEr/XjOYPrJgL/Ltoyf42yousf9XjPpBVFL09E65nbHJcky/+G28ulyvvRryp4NGbJ+fJeobM2o/v9/n0/7X4DDrON4IKpGxX9ojIkviDoXf+9v69fumJ6TPEy+rYX7ZzDRRAe1RZB/fdNarc48+IeG7lFPniPAN7FG43DoWEV/l5n8gqjjbCtyOlR7X/quS5Nl+egOUrKOJf5Y9myYdU8rdzn/ePFQDYvWjOkkh8Lc/AdwFK7E6dB3zX9rVitRd0zzgrgGoval5z3Yzu2Ep1YGlNmrpjc5f24qLz2a6i4vV4Z5VvE8VrhtZg9Z8HA7yb+uqYy+tonL5Ftbuhf9qNUX4gFwXMqkyGqB46H/mv+b1k/dQhFeDgAAvVEF3q8POgvnQwkiI7/vDIqlvBgAAMa0C16s5n4c0Ph9f+t+XggAAONWAu7BAU02/0I7pGObXwAAOC7O3G9n4IQmmv+WQUlulyheAgAAU/lKiqwUHNEk81/b+1SJhN5g8AMAGM9W2ZH9Q5zRmH3/UC6DHgAADvM4zmiC+RdlDRB1VSQDHgAAvq4HCIf64ZBaf/nbP5Mi+2MGOwAAfOtUwEfqIjicUtuvf2shAx0AAI6SBCzAKfXc97+GAQ4AAMfG/iOOqZP5b81q4AS2lIENAADHoUyKshrjnFp8+aee7AS0kEENAADVJMLRQC32/UOjGMwAAFAzrIdw0GCbf2+h1S8AANScgxLO7ImTBvPI32lc8QsAALU/FWC9J9sHno6jBu/r/ykGMAAAnCCjcNQgmX/Y7uAu3zBwAQDgxDggW61UnDUI5r+29w+cgG1j0AIAQJQaBL2hTpThsL5f+rfuYsACAECUuQ2H9bP5F2Y2coJUzkAFAIAos1c1lcNp/Wj+kvA9CYdWM0gBACBGrFVeg+P6bunfHsrgBIB4c2CLJZ8uHyBvvdBLCqd0k9X5nWTho6ky657WMv6GZjL62ibyyNUN5f7fNZC7Lk2Wmy5IlBGD6v2H4Vn1ZEj6ef/57zdfmOj+e/f+tr488seGkvPnpvL0zc3lmbtbyfxH2smrzp9fOLWrvPNiH/m38/ceKLCIQ3wbBF2F4/rqzH/ar53AfMXABIBYsN8x+Q8X9ZPw1G6y8LFUmXRLC3n06kZyy0WJ8qe08zxlaHodN2FQicKz97WWlbkd5Y1ZPeTjV/q5Pzfxizb2btmWdS7O65+v//kMSgCIBsVr0+TN53rKksfby7gbmrvmOsQxWa+Nvjaon/vey+vL1NtauCsHO+f1lopNmcT5xBsEzcF5/WD+W+2+DEgAqA2HCi35x4K+siKng2v2t16UFEijr+mKwV+uqC/T7mwpa8Z0kn8t7c9YqBVZA3BgL81/bvZJztf/mwxEAKiW4Yct9ytYfd2rJXO1/6674VcHVXcw+bYW8trTneXzlQMYK9Xjr6rvDE7s2dJ/6M8MQgA4FrvXpMvGiV1k4s0t3CI7DP/4qG2PmXe3ku2zelBHcOx6gKE4sRfm/6b1UycAnzMAAeDbqGXtRaPaywO/b+BW2GPqtUetkqhTCOrkwd7XqB/4Fp/J64POwpHjX/iXz+CDb1OyNk3+77me8spTHWTKbS3cZd6Hr2roHql6yPmnOpKlvgRffqy9bJvZQ75cNZDnpgn/XNzPPX533xX1Me4YMSyzjuQObyKbJ3WVio0ZjLsqnsKR41r4ZzV1EoD9DDxQfLFqgCzP6eAey6pNtfbIK+u7CcFHSyiGCuLxvHVjO7sJHgYd/5WBaXe0lLfm9JLKsMnbBMqLshrjzPH7+l/G5AcfLOorU29vKUMzondEa9SQxu4Z6sowz9fvqDip4jXM2HtuvzhZXno0Vb581dAVtXBoMc4cl6Y/lsXkZzafrRgoY65vFtMJTXVue39hX563D1HJ2fyH27K379MjhhNubOZ2RTQuiQ5npuPQMTX/1JOdB/02k6CZHCwIuYVd11p14tZE5dl7W0s5e52+Qo0BzNb/3Hd5A1k/vovbKtmQsfk3rgyO6dK/dQMToJl8tTrNXZ73YiK7+7IUt8CMOHjP1md68OUfMFS7ZFWjY0QiHbGuw6ljYf47ss+QcOhTJkHzUMuJNw72dq/3WquuW/lMPLxDfUne+ZsUTDWgqB4Mix9P1T0R+Fw2Zp2JY0d9+T90D5OgmYVe8VryP/6WwHnulwxx8QZV7Y+RBp8bnGR++egO+jYYili349hRNf/+P3Ee7JdMgmaxeWJXt6jIbxOYug2O+MSfJ4Y2xkA14rbsJHdVTcNiwS+kIOPHOHe0EoCw/QAToFm8+WzPqB7vizbqylXiFD9UB7qhAb2RD47NU8OauO2aNVsFuBfnjob5Fw4+x3mgxUyC5qCO3w236/r8mtXzpGBKN+IVxy5/mKXelxH9vxd769QcaLdsTjsbBz/xpj+PMQGaQ/Ha9MA0d1G1CR8u4nRAPFDtnTFKvflzqK68u6CPTs2BHsTBT8T8t2X83HmQJUyApjR4sdze/UGatNQRwfJN9AmINX97oRcmaUiBoGr0pcm4LZXtg3+Bk9f+6z+Hyc8cVGVwECetGXe1In5xuN0PgzQDdWGXRmN3FE5eq8r/tF87D28vk5857X39ctyvNvz1+V7EMYbs25wZ6PEBNUPd1KnJ2N0r27LOxdFr3vN/HBOfOeRf3zTQE5baCjCo5aknxPr+B/APT17TWKeCwBwcvUZ7/1nnOg+ugknPnGY/OkxaNAmKLZsmdcEcDUGdslHXfGsydsulIOuXODuV/3CEm93u/10DPQqYBtWjIDCWrYALLLnjkmSNTa+OPHp1I1kzppP8fX4fefO5nlI4pZusHddJlj7ZQeY92E5m3t1KJtzU3P33VI99nZOAjRO7aHQiwH4AZ6+O+W8feLrbSYkJzwjUXp9Ok9ayp2gQFEuUIfrJsGP1Z6vTMB8v7X/c56Ha6X7ySn+3BmXduM5ukpA7vIncfGFS4N+lF53fRaOx+6XyNhz+uF3/QiOY6MzhoasaapUA3ORMvKpgjdjGjqm3tYh7XG+/JNm9537SLS3kxsH14vJ3XpN5nmvoFZtqN55Udz3VP+GVpzrI0zc3l1svClZSoJ61VmM3bF+Lwx/L/OdmnyRF9t+Z5Mxg57zeWi5dqr1q4hs7lCGqIrFY32X/7H2tJTy1m2uk6kv7mbtbeTKe7r28vny0pH9Unt2nywe4S+vT7mwpd1zi75sV1c+o2dh9V3kcTn/0nv8XM8GZwzN3tdYyAXh8aGPiG4djgWNGRO9UgLpuevJtLdz2ziVr075jmiOvrO/pmBqeVU/C06LfevrzlQNkdX5nd8thWKa/jlk+/5c2+o3dsHUBTn/05f8tTG7mfMVdZ9fTtoBJ7csS59gXkL6a38k1x9p+Wb/0aKrbfvZQ2DpqA6Jbs5N8Uxkfy0uoVAFrZHp3d4ults80mqjbQDUct4U4/ZHMf6vVg0mNYi5dePmx9sQ5jvdHzH+4rdx0QWK1lvZVbKqzpK62qEYM8l+Suvjx1LissKjtD7XK4tXKgEbHAL+9CtAVx//O0T9rIZOZOUy+taXWCcCDf2hInOOM+opXpr0ip4N7XE4Vvilmj2wjGyZ0cZfya9J62I/m/zWr4ngdddn6dPfvUysmtAOOSmOg+Tj+N82/INTQeTCHmMTMmajVpR+6NzLZtSaNeAeQXavT3Kp/rqP+7pbL23N7y8SbW8jQ9NiuCrw9p7fOY+yQbM1qgPP/5+s/NIGJh+p/7RqZPM1pgKChqv0f/H0wjqaquxHeX9jXk+ekigfVysq1Vt2o/15Tbmuh/1iLWONwfmX+O7LPEK785dY/DVGnHIh3sFCV51xHXbPVEtWwJ1oFvSr52r/FiD4apbIx60wSgCJ7KBOPWah9WRMSANXimHgHB9V6Vy2tB22cTb/D++uoyzZkyNwH28qwE7ix8clhjd0/x5gxF7GvJgEoCkWYfMzizt+kGJEAqH3S2nZxg/hSvjEj0L3133y2py+eo9oamHZHSxmaUf1E4M+hurLw0VQ5WGDcuDP7SKAUhloz+Zg30QbxK6u2vOfRHi3UjBdGtgn0OLvr0mS3fsEvz1OduFDbKernOtrPfM9lKe7xTdVp0dixF85sQ/EfGMM/F/cz6lpT1ViFuPsb1ROgJl+sfmXJE/7sPfHZioGyY3ZP99TClsld5a05vdz/jbHnMsZM89+c/SPnl9/FADCLN2b1MCoBUGfSibu/GRvFlsJetwsuXZ9OTIPVE2C3ROzTTGz7+weCbx7qrnOTEgAt+5lrtiKl05bUolF0oAxgZ8DLTVz+30zwzUO1YTUpAVBNU4g7J1LixfXn15U9JlXS67EKsN60vv9NCbqZqDPDJiUAY65vRtx9yler02Le0c4L1Cob8Q0YjieakwBEQrkE3Uyeu7eNUQmAOttM3P3Jksfb038C/NIZ8AkzzH9t71OdX/gLgm4mqmmJSQnAI3/kUiA/ovraH+uIWtD5YBHHTwPGZ7Ij+4cGFP9ZFxBsc5lxp1kJwKNXNyLu3EcRd+bcT/Fp8IoBQ7YJxX8vEGyDe63fZ9YWwFPDmhB3H6Ia0Og87tTqBnEOXDHgLM33/u3T3EsQCLaxzHvIrCJAdcacuPuPv1xRX/ux9+/lA4h1sChR/XE0Xv63LybIZrNoVKpRCcCkWzgG6De+WDXQiLG3Krcj8Q4ahaHBOi//zyPIZrN+fBejEoC5D7Ql7j6jcEo3I8behJuaE+/gMVtP898+8HTnlysjwGbz1+d7GZUArM7nTLbfmPNAWyPG3u2XUAcQQPYor9Tw69++lODCJ6/0NyoBeH0mlwH5jVFDGhsz/orXphHz4PUEyNYwAbAWElzYvyVTy+5rR0P1mifu/uI6u54x40+tuBHzwPGiXua/MetM55cqJ7BgSgW24lqrjhwsIN5+Qt2WZ9IK1PrxnYl78CiXgowf67T8fwVBBdO6AdIEyH+8v7CvUQnAgofbEfdg9gS4VKerfxcTUPiaNWPNuBJ49ki6sfmNrTO6G5UATL6NY6gB5SU9zH9H9hnOL1NBQOFr1L64CZNvZDoFgH5j7bhORiUAXEYV4G2AiH2aDsV/WQQTvs0dlyRrPfEOzajDvew+ZHlOB7Muo7qay6gCvA2QoUP3v/EEEr7NrHta6/3ldQ1fXnSi9J6RV9Yn7sFNAPJ16P73LoGEb7N9Vg+tJ94VzpcmcfYful8CxKVAOvUDCL0T9Mt/mhBIOBKHCi25+cJEbZf/d62mAYsfMe0yqjt/k0Lcg8zWrAZBPv53I0GEo/Hig3pOxtwA6OctgPZsAUCQGB7k5f8VBBCOxsdL9WwLTPtfigApAoQo1QEsCab5b87+kfML7CWAcCxyhzfRbs9VbW8QW44BcgwQosBe5aUB3P+3LIIHx+PdBX20mnA3TuxCXH2M6s1gUgIw6RYaAQW/GNAeGMTl/7EED6qD+krR5frVAwV8/fuZ9wxrBTz/EVoBBx9rdBALAP9O4KC6/dmHaHBDYOGUbsTT55SsM+syoHXjuAxIA94KlvlvzWpA0KAmzLw72BcEqTvmK8PE0e+oGA3P4jpgCBhbBiUFqf3vVQQNaoK6pvWGwYmBPff/0ZL+xDEgqGTNlASgeG06MdfjNMAVQdr/n0rAoKYE9aa2JU+0J34BYs79bYww/9svpgugRnUATwcpAXibgEFteCZgWwGPD20sh8IU/gWJgindjEgAJtxIQyqN+L+gtP/9mfPDVhIwqA37Nme63cuCMMHedEGifEXL38DxxaoBRiQAK3M6Em99qJTNaWdz/S9oz641ae7ypZ8n12utum4PA+IVTO67vIH2CcAnr1CXohmZQVj+H0Wg4ERRRXXXn1/Xn0V/6XVk28wexCnAzHtQ70uBuARIy0LAh4OwArCRQEE02Dmvt++SgGsyz5PCqV2JT8D5fy/21joBmD2yNXHWj3X+Nv+dGac4P2Q5gYJorgTccpE/jgcOs/jy16cfgCV3XJKsbQKgOh4SZ+3YKzuyf+jfBCBsdSVIEG0+XT5A7v+dt3u2t2UnseevGbpeDcwVwBoTyezk5/3/WwkSxIL9WyyZPdKb89vqrgIaquh4GmCgFi2ov82r+Z2Ir7YJQOgmP+//LyRIENNmQc/0iNsJgRGD6rnXx1Zyzl9bxt/QTCvzvy6rnuzZkEFs9S0EnO/nFYBPCBDEmopNme4tZ8PtujFr7TvjrlZSspYz/rrzwSJ1EZU+CcDCR1OJq978y5/mvy3rXIID8WTva5nucuet2UlRmTzVJTFqm0EtDfN8zSH/uqZamL9KiNVth8RUc8KZv/JhB0DLIjjgBQcKLPfWM3Wj4M0X1iwZUMcMJ93SQiLTu7srCzxPM1cBhmpQC6CKGomnEQlAug8TgNA9BAf8wJevDpQ3ZvWQpU+0lzkPtJUZd7aSp29uLtPuaOl+4auJUhm+Ol3AFb6geO7eYF8QdPslyW4bbWJpQiGgfYcP9/9BtCvJAAAgAElEQVTt+QQHAIKIKpy76cKkwCYAKuEljqYkANYcP24BvEdwACCwJ0wCeh315FtbEj+zjgK+4y/zL8j4sXADIAAEnFn3tA5cz39VDEvsjOKQbB94un8SgK12Z4ICAEEnSNdRD8usQ3dKU9lqpfpp//+PBAUAdOCr1Wlu62c/m7/qXbB5EpdSGcyVfmoA9BQBAQBd8PN11IplT3YgTkZjP+anFYBlBAQAdOLtub3lOrue78x/wcPtiA8s8tMKwIcEBAB04/2FfeXGwYm+WfZfPpovf3B51x/mv33g6ZwAAABd+Xhpf7n3t94WBl5r1WXPH/73JMDa3qd6nwAUhloTDADQmYqNGe55ey/M/57LUuSfi/sRB/j2SYCmftj/v5BgAIAJbJ7YNW4dA9X9BLNHtpbyTVzvC0cgHLL90AHwdoIBAKag2garuwOuyYyd+Y8a0lg+XMRXPxzzJMCNfrgEaBKBAADTKF6b7l4sNWJQvagV+Y2+tgl9/aG6jPU+AQiHVhMIADAV1Yp3y5RuMv6GZm6xXk1N/5E/NnSr+z9bMZDnCTXZAljOJUAAAD5h/xbLPTq4YUIX9+rpSbe0kNzhTVyTf8r5up9wYzN55u5Wsjyng/zthV5Stj6d5wa1w+tLgURGfl+K7P0EAwAAIK6UiyR8z7sEYFvWuQQBAADAA7YP/oWHy/+ZnQgCAACAJ70AUj3sARC6iCAAAAB4UQdgD/KyCdCNBAEAAMCTBOB6L08APEEQAAAAPGGUl02AniUAAAAAXvQCsGd4WQOwiiAAAAB4gb3MywRgOwEAAADwhG1eJgD/JgAAAACe8C9vzH9u9knOX36QAAAAAHjCAU+6Acq2jJ/z8AEAADxkc9rZ8U8ACjMb8fABAAC8xErxYv+/Iw8eAADAQ7xoBywReyAPHwAAwMteAKF+8U8AwvbFPHwAAABPewFc6MEWgDWEBw8AAOBpAvBHL1YAbuHBAwAAeEgkdJMXRYAjefgAAABeJgDWvV4kAKN4+AAAAJ6uADziRQIwhocPAADgaQKQ60UCMJWHDwAA4GkCMMmLBGA2Dx8AAMDTBOBZL44BLuThAwAAeJoALPBiBeAVHj4AAICHhEOLvUgAVvDwAQAAvMRe5kUC8CoPHgAAwEuslV4kAGt58AAAAJ5uAaz2oBVwaAMPHwAAwNMtgPVerABs4sEDAAB4ugWwkQQAAADAPDZ5kQC8xoMHAAAwbwuAIkAAAABvE4A1HAMEAADgGCCNgAAAAAxYAfCkERCtgAEAALztA+BJK+CXefgAAACe8hLXAQMAAJiGN9cBh6bx8AEAADzdApjsRQIwlocPAADgaQKQ50UC8DgPHwAAwNME4FEvEoCRPHw4FpUFmXJoY5ocem2gVG5KFynM5LkAAEQ1AbDv8yIBuJWHD9/k0PoBUjG/g+yZ3kJKxqZIcW7SdygZV9/9v5fPTZUDK3q6SQLPDgCgtkWA1s0eJADWEB4+KA6s7CVlU5oc0fCPS36y7JnRQvYv7U4yAABQY+w/xj8BCNsX8+ANX+LfnCF7nmlZO+M/0urAmBSpmNfe+XPTeb4AANVLAC6MfwIQsQfy4E1e7u8vpRMaRc38v50I7FvYWRW38KwBAI5dBNjPixqAjjx8Q7/8N6VJ6fgGMTH/b1I6sZEcWNWbZw4AcNQaALtd/BOAwsxGPHwDKbSkdHLjmJv/Nyl/IdX9e3n+AADfxkqJfwKwLePnPHjzqFjQMa7m/zVlU5tVHSUkBgAA3/goG3xO/BOAudknOX/5QQJgVtFfSX6KJwmAWxswvqEcXNOXWAAAVHFAZOT3E7yQhEOfEgBz2PdyZ8/M/5vHBg+s6EU8AACKQv9K8EpSZL9JAMyhdFIT7xMARZ6TBKykOBAAjGebhwlAaBUBMGf53xfmz0oAAMDXPQCWeZcARELPEgAzUG17fZUAHF4JOLi6D/EBAFN5xssVgKcIAPv/XlIyroF74RAxAgDzegBYT3i5AnATQTCD8hfb+zIBcI8ITm4qldw0CACmEQ6N8DABsLIJghnsfaGtbxMAxd7n2hAnADCsB0BosHcJwFa7M0EwZAVgTqqvEwDF/sXdiBUAGJQAZLb3LgHYHDqPIJiBuqXP7wmAukSIegAAMIbtg3/hXQLgdgO09xMIA4oAF3b2fQKg2DOjOfECABOoEEn4XoKXcn6I9wmECccAewUiAVDsW9SVmAGA7uxM8FrOD7GWQOjPoQ0DA5MAqK2Ays1cHAQAWrPC+wQgHJpMIEzAco01KElA+Qvtgr3issWSXWvS5J+L+8lbc3pJZHp32TKlm6wf30WW53SQJY+3l/kPtz0iCx9NlWVPdZSVOR3df3/TpC7yxqwesnNeb/n4lX5SvDZdDhRwvTJAsI8A2uO9TwAi9h0Ewwz2zGwVmASgODdZDq3v78/VlEJLPl0+wDX2157uLAsfS5Wpt7eUx4c2lrsvS5Hr7Hryp7TzYs5NFybJ/b9rIPnXN5WZd7dyk4rCqV3lvYV9pWxDBmMewN9NgG72wxbARQTDkELARV0ClAAkOQlLS2+NPmy5X9zq633x46ky6ZYWruEOs+rExeBPlBsG1ZPH/tRIZt3TWtaO6yTvvNhH9pAYAPgE+3wfJABZbQkEdQB+5eDqvnF5NpXhkPtVr76g5zzQ1v2aH55VLxBGX1PUKsXk21rIq/md5N0FfdztCt4PgLhvATT3PgHYmHUmwTCH0omNg7UK8EzLmJr+317o5S6f33RBopZmXx3+HKorOcObunUH7y/s66588K4AxJRKidinJfhBEgl9REAM6Qj4YvvgrQLEoBZAFeepr3xTTf9YqJWP0dc2+U9CoBIl3h2AqO7/v5fgF6njCATFkH4Aq3oHLgHY+3zbqD4DVY1/TSZGX11uvzhZZo9s466WqAJI3iOAE97/X+KjBMDOISCm7DuFpGRs/WAlAXlJcmhTdPoCqGK4IemYem25NTtJnr+vjbw9pzdbBQC153H/JADh0J8IiEHHAWe1CtwqQMX8Dif8e//jpb58+UfzGOIFiW79hOpPwHsFUKMCwN/7KAGwuhIUg44DvtwlcAlA6YSGzktT+y9OtXR9z2UpGHeMuPfy+m6Do+K1XOYEUI0EoIN/EoDXB51FUMzh4Np+gUsAFAde7VPr3zk8tRtGHQeGptdxCwhV7wTqBQCOcgJgY9aZCX6ScCmQQdlnsNoC/6cYcHbtiwFHDaHiP97clp0ky0d3oPkQwP+yM8Fvcn6olwiMQXUAM5oHLgEoGdugVtsA+7dkyrDMOpiyh8cKZ93TSj5Z1p93D6Ao9KL/EoCwfR+BMYeKeR0CuQ1Qm86AqkgNI/bH9sDTNzd3izF5B8FcrLt8mACEbAJjDvtf6R7IBEA1Mqrp7/r6zO4YsM9QdQIkAmBoD4AM/yUABRl1CIxB9wKsGxDIBKD06UY1/l23ziAB8HMioG4v5J0Ec7oApv06wY9yfrjPCJA5DYGK85MDmQQc2jiwRr+r6mCH2foX1Zhp3A3N5eOl1AiA9vw7wa9yfrhFBMgcSic1CWQCsG9Jtxr9nmXr0zHaINQIZNRxiwVL6CUA+vKSfxOAiHU7ATLoJMDMloFMAPY+27rGv+sdl9AEKCiMGFRPVuZ0lAMF9BEA7RoA3eLjBMDuTpDMoXxOu0AmACXj6tf4OOD8R9phrgHj7stSZMfzPXlXQR8KQ138mwDszDjF+SErCJQhRwEXdAxkAuDWAawfUKPf9dPlA9wlZow1eEy9rQUthkEHKpTHJvhZzg+5mUAZchRwabfAJgD7F3er8e/73L1tMNQAbwtsntSV9xaCXHi9IcHvkoj1BMEygwMrewc2Adj7Qs3bAqtiwDsuScZQA8yYEc1k95p03l8IYgLwaAASAHsQwTKDg6v7BDYBKJ3cuFa/8weL+spwuy5mGmBuHJwo22f14B2GgO3/26EgJAA/E3VbEQHTPwFY1z+wCUBxXrJUFmTW6vdWrYHVkrJXBqbuJbjB+fvvujRZ7v9dA3noqoZH5N7f1nf/nZsvTJJhFvUL3+4dMOeBtpwUgKBQKZvTzk4IgiQSeoeAGdAN8LWBwU0ATvB64I9f6eeab1QvvbHryl+uqC9jrm8ms0e2lpW5HWXLlG5uJfs/F/dzl65PxLD2b7GkeG26+2epL+B14zrLS4+myrQ7WsqTwxrLPZelyLWGJQr51zV1nwvvM/i7+5+1IyEocn7Y6QRNfyo3pQU6Adi3qMuJ1UA4ZqxM+ibnC7smpnOdXU8eH9pYZt3TWlbnd3I7De5a7Y8q9cqw5Z54UO2PX36svYy/oZm7iqC+mHVNAp4a1oSVAPB5AhCaFKAEwL6aoBmwArAx2AlA+ZzU6BRDOl+Q4WndZPKtLV2z/Ka5XH9+XXn06kby/F/auFXoql1tZTh4ZlO+KcPd+lie00Hyr2/q/l46JQHzH27LOw1+XgH4XZASgCYEzYAEYEOwtwD2TG8em+fiGPyeDRlSvjFD39g7v+MHL/eVVbkd3T78XtZERKcmoI6b4PBegz8TgIz6CUGS80O/S+B0TwD6BzoBKBnXgDhGMSFQBqq+pFUtQVC3Aogl+HD5/52EoMn5wScQPN1PAfQLdAKgqNycQSxjgDouuWhUexl5Zf1AJQEfLupH/MBn2PkBTADs8wmc5o2AXu0T+ATg4Bom/Fjzr6X93ZWBm2tYLOkFqvCRmIHPEoCM4CUA2weezr0AmrcCfqV74BOAAyu4LCZuK0YFIXl9Znf3ZIFf71V4YmhjYgV+olwi9mkJQZSEQ6sJoL7sW9g58AnAvkX0h/eCL18d6N6weMPgRF8lAOrnIT7go/a/yxOCKucXuJUg6kv53PaBTwAq5nUgll6uIm3JlNcmdPFNrYDqmEhcwD9YNwQ4AbBaEEB92ftsq8AnAHufb0MsfdGAKCRvzOohD1/V0NMEYGh6HfdnISbgD7IaJwRZzi/xAUHUk9KJTQKfAOyZ3oJY+oy/Pt9LHvtTI08SANXIiRiAT5r/vJcQdKkWhgRTQwotKc5LCnwCUDalKbH0KWpF4L7LG8T9bgCePfhj/98eH/wEIGxdQDB17AHQP/DmfyLXAkP8GgxtmNBFbrkoPsWC6oIknjv4pADQDn4CUJDxYymy9xNQzYq3lnTTIwGY2Ih4BqHe5LVMmT2yjbtHH8trlsvWp/O8wQ9UyI7sMxJ0kJMALCOgmk3Iz7XWIwGY0JB4BqzDYKwKBec91I5nDH75+l+coIucX+YPBFWzAkDHOHVIAErG1SeeQdsWKLTcS4iGZ0XvAqI7f5Mi+zZn8nzBL93/rtAnAXh90Fl0BdRoAn5toBbm7yYAY1KIaUD5YtUAGTWk8Qmbv7rJ8P2FfXmm4J/l/0j/nyToJLWkQWA16QD4cmd9EoCxrAAEfTVAXTp0TWbtzF8VF/5zMfdBgK94KUE3qSUNAqsHZVOb6pMAjKcGQAc+WtJfHr26Zr0Dpt3ZUso2cBsk+G75/1L9EoCNWWeKutiAAAf7i2tjmjbmzykA/fjHS31lxl2t5PZLko9o+up/n/NAW/eGQp4X+JA92lT/H6E18EICHPDl/4WdtUoAyqY2I66aUrI2zd3b3zmvt8sevvbB/7yYoKvU0gYBDvLRFEtKJzTSKgHYM7MVcQUAfxCxsvVNALYPPN35JcsIdDA5sKKnVuavKH+Bs98A4JPlf8cjE3SW80vOI9DBZM+MFtolAGpLg9gCgA+YnaC7JGxfTKCDx8E1fbUzf8WBFb2IL9SOQksqt2S4hbGVm9Kc/83imcAJjKfQYP0TgIh9mvPL7iLgfP37AdXUiPjC8WpfDq0fIPsWd5Xy2W3dwtGSsSlHGE/JUjK+gZRNaeJuLe1/pbubIPAMoRp8KWt7n5pggiRijSPgAdr7X9VHS/NX1xmryZ0Yw/9+iWXKwdV9peKlTrJnZku3WVStx1h+sux9tpW7gsazhaMX/4VyE0yRbM1qRdCD8/VTNrmplglA6SSuAoaQVG7OcAtcy19s737dK9OOzYmTlnJoIytOcMTl/9YJJkmKrCICz7l/L9n7QltibGIzqw0DZP/SbrL3+bZSOrFx3O+eUFsDxAH++5EV2pJgmpwEYAjB93vXv4HuhKVrAqBMgDjrX6inlt9VIqt6PqjbH/0w9irmdyQ2cBjrKvMSgB3ZZzi/fAnB9+/S/57pLbQ1f7cA0PkSJNaaLedvyXBPdlTM6yBl09Ryvn8TWJIAcChVbfITTJTzy09lAPiTigUdtTb/krENiLMmq1RqSV1V3auajuK85GCtQi3rSRyNxp6YYKpkq92ZAeDHqv/e7pEmnROAvc+1IdYBXJU6uLaf7Hu5i1tZr25yDH4imuL2ESC+xp44aZ9gsiQSeoOB4LN9/3ENtDZ/vrwCspxfkOkmo2qpXG1H6VqPsndWa+JtJtsTTJdE7OsZCH7ZP02Pe1W0N+f/k11zIeY+Sz43pTuJWQ8pn9Pu8NHTZP3H4mHoE2DiipZ9LQnA64POEnUJAgPC8+Yn7hloAybbPc+0JN5+6K63TnXX6+Jux5ROaGiM2bMKAA575U3rpwnILQacxoDw8MvfMX9dW/0ecfl/eQ/i7sEYO7i6j1Qs6OQmYEdupWsweUmH7xNgrBhy9G8Kzv/fbYAmzkOpZFB4s8/qHpcyZKJVvdolTNxj310vvaq73lzVXa+pa3AYPTdTgkulFJzfDOf/31WAVxgY8T8z7U7OBk2yFfM7EPtY7N+vHyD7l3St6q73dCMMvTZbU9NbMJbMYBGO/51rgkP9GBjxrPZPqzo3bdgyqyo0I/5R6K63us/h7notfdNdL/DkU5xqSPFfLxz/yKsA2xgg8flaKx3fwLgJVjWLIf61PY7Xp+o43ozmvu6uF/jTAE5ixZjTmghOf9RVAOtyBkiMm/y82sfMAizHtPj6r6bhb0pz+ySUz02VsilNA9ddL9B1AIu6Mgb1Lv77DU5/1GLA1JOdh/QBgyQ2qOr3WF116vuv/xfbMwaO1l1vzeHuerNaG9EEytfjdA6rVBrzvqzt/QOc/tjbALcyUKLPvkVdjP2SU6amCh4ZB9/srtdB9kxvrvVtj4HsB/As/QA0/vq/AYc/XgJQkPFjKbJ3M1iieLHPvA5GT6omt/1VxZ7uZTlzUqVsUhOjuusF8iTADE4CaEqx8jYcvnqrAE8xYKKzvKsK34yeUGe1MukLQw6u7+/uI9NdL6hHAZszb2k5F4cexdmr3xionhTZ+xk4JzTgXBMweTJVx9N07q7mLue/+nV3vRYs5+uQAMykTbWG7JPNofNw9hqtAlhTGDi1//JXE4nZrVWT3b1uvarz079VnY9halcD8DzXVGt47n88jl6rVYBQBQOo5l+FJvX1P2rHP+erOPD7968NlP1Lu0v57LZSOrEJBmnCuH2pE/OYXpRLQUYdHL1WSYA1jgFEa99aLaOGreAdx1vd1zWAqsty6K5nIgdW9GIu04lIKBcnr3UCkPZr99pEBlL1zH8KX4nqGQShnep3uuvRbAdoBazflb/bss7FyU+oFsDOYSAdz/zTpWwy5l86sZG7T+7L5fwNajm/m+yd3c75ORtjdvDdlatnKADUjMdx8BNNALZl/Nx5kKUMJsz/mBX/Y+u7JuuXExgH1/Q9fFlOK7rrAcv/5lEq2wf/AgePTl+AUQwozP/oeFvxX7klUw6s7OUu55dNay4lXJYDNV29mtQ4eHUrcKyeHA/h3NFKAAoHn+N2UmJg/dd0Nmcc7uzG5KmMN77d9QYe7q7XTkonN2b/Hk78639lb+Y1bbB3y+a0s3HuaCYBYfsBBtZ/vzjLJlPt7y79j0mJcZ9/Sw6u7VfVXe/Z1lIynu56EOWz/89x9l+zc//34dhRPxHQ/yfOw/3S+MFV6Jj/tGZMnP+ZPKN7ecq3q/PprgexLVxtTOW/XuyS1wedhWPHpi/A7XT4a8nE+c3rU19IPcHuemmyf1kPdznf7a7HZTkQL/Mf38DdTsI0tfr6vwWnjlUCsCP7hxIJvWPq4FJtQpk4vzWJTmhY/S8oJ4E6tG4Al+WA9+P26Ub+ObUC0dr7/7vszDgFp45pQWBosImDq3xueybOozX/mdREDqzo+Z1aAHUVriquqrosR3XXYzkffDBepzeTys3pGKZ+F7DZOHRcjgVaK00aWBUvdWbirOZxQNUPwIWjeODDTn9Vd1Rw3E9DXsWZ43cioLnzwA+YMLD2L+/JMTOAgN9MqRpCseSvLQclktkSZ45vc6AJug+sg+v6UYUOEOAv/r2z2zrGPwCT1JsxOHK8E4DNaWfrfCxQ9bRXVcJMpADBakmt+kWokyWqXwfmqD1fScT+GY7sySqAfaOux/3KpnLWH8D3hj+ugVtgqup0VMMo2vkax3Cc2LO+AKknOwF4W7vjfs9x3A/An8dOG7nHcfcv6cqePvxNeRBO7G1zIEunQaXOqDPRAvjnvL5KyPct6UbTHvjWSm1mOg7sj62AJToMKNWkppjjawCeHSMtndhEyme3lf1Lu8uhTZzVh6PeEbIQ5/XNKoBdzwlKSaCL/goy3b7gTMIA8Tqel+S2fy6fmyr7l/WM8aVSoBHFEj6/Ls7rq94AoRG0+QWAoxbs5adI2bTmUjGvvXvhk7pYCzODWvT7vxbH9VsCICO/7wRnUyCb/SzrwQQNEIOrotWNjupmxyrDp0IfTrjd7xblNTiuP7cCmjhBqgjUvv/GNJr9AETpSN7eZ1u5hbQH1/XnSB5Em31ScH4znNbXWwH2A0EaVKpFKJM3QC0Mf/zXht+l6gw+BgWxXfq/D4f1ewLgXhls7QjG0n9PJnIAjuSB/3mLq36DkgRstTs7ATvk96r/kvHcRw9w3CN5qkJ/MxX64BmOl2R1w1mD1SBonJ8HVfkL7ZjkATiSB/4v/MvDUYOWABRk/NgJ3oe+vOVvTV+u+AUq9FWF/oKOcnA1R/LAt3wgG7POxFGDmAQU2RlOACt9V/g3vTkmABzJw1zA31RKxB6IkwY7Ccj306A6sKo3hgDckgfg/3a/o3HQoCcAOzNOcYK53S+DqmxqUwwCOJIH4G/+Kpuzf4SD6tEboLkT0L2ef/0v59gfcCQPwOdUyNasVjinXlsBN3pbSWpJ2aQmmAdwJA/Az0Ss63BM3RIASfieE9ylnn39r+DrH4JD1aU5HeTAyl5uzwqMAQw58rdceQWOqeXRwKxfOkH+tyeV/zOo/IcAJQBTm7nHVTEFMIjPJJz5K5xS762A8+N+4c+GgZgKBBK17M8KABhx5C8csnFIM5KAiXHt+vdie8wEglvwN6FRVbMeTAL0ZQzOaEoCsH3g6e7lDvEYWIWZUjK2PkYCgS8E3PdyF4wCOPKHdFgFyGrsBL445jf+Le2GeYA+WwIvpNLUB3SiRLZaTXFEE5OAiD0o1q2Cy6Y1wzhAK/bMaqWqpTEPCP6+f5F9IU5odBJgPRGzK383p7tLp5gG6IZqAoSBQLCxH8YBTU8A5maf5AyGFbEYYPsWd8EsQFsq5nfARCCovKrmfhwQJUjh4HMkYr0X/bP/LTAK0JoDK3phJhC8K34j9s9wPvSNosBQR7cHdBRb/5bkp2ASoP2tf5VbaA0MgaFcCjPb43joCEmANYRrfwFqeDJgTjuMBYKy7/9HnA4dKwmYEo2BpvqoYw5gBHlJcug1bgQEv2M9jcOhYycAa3uf6gyUIo7/AdRgFWBuKgYDfv7yL5CdGafgcKgaRwPTfu0WitT+Rin2/8GsWoAxKSKFNAgCP17vG/pICjLq4Gyo+klA2G7uDJ5dtRlwB9f1wxTAvBMBq3pjNuA3imVrViscDdViJcDq4wygfTVv/9sdQwADiwHZBgBfLfvvl6KsATgZOpGiwKtqfPvfXG7/AwNbBM9ogemAj673tX+Pg6EorASEHqlRA6CZLTEEMLInAMYD/tj3t+7HuVB0EgBJ+J4U2bOqO/hKJzbGEMDA44DJGA/4gdlqzsa5UPSSgB3ZP3SSgDXVGYCcAABTwXzA433/9Rz3Q7FJAjanne0MsrePfwMgRgAmkuy2wMaEwCPekjetn+JUKIb1ABn1JRz69KhHANf3xwjAzBqA8Q0xIfCKT6TQTsahUBySgMyWzoD74sh3APTBDMBIyqY0xYjAC3ZJOLMNzoTilwRU3R5Y8p0eAMt6YAZgJHtntcaMIP6NfsJ2BxwJxT8JCFtdnQFY9s0BuW9xV8wAjKTipU4YEsSTPc6Xf0+cCHm4EmD1d++Y/joBeLkLZgC0AgaILfukyM7AgZAPkgD7fGdAHnCvAV7QETMA8woA81OksjATY4J4cFAiVjbOg/xUE3CRGpgV8ztgCGBeG+BZrTAmiAeHJGJfhuMgH9YE2L+vmEcCAOaxf1lPzAli39+/yBqC0yDfas/MlsswBDDu/H8Yg4IYE7ZvwWGQr1WckzQSUwCT2LewM+YEMf7yt2/EXZDvtTs36XZMAUyhdHwDiv8gxgV/9tU4CwpGApCXPARjAHP2/ntgUhA78y8KXYmroCAlABdjDGBE5f9MKv8hhuf8w9YFOAoK2BZA8gDMAbRf+p/QUCo3Z2BUEJsOfxF7IG6CglcEmJvSAYMArav+x6TIwXX9MCqIBaWy1e6Lk6BgJgCj6zfAJEBb8pPlwMpeGBXEgq8kktkJF0GBVcmTjX6GUYCuX/6YP8SIf8vWrFY4CAq0ZGTCD4pzEw9gGKBbs5+D6/pjVBALdkpBqCHugTSpA0h6F9MAXSib3kwqN6VhVBALNknE/hmugfRJAPISV2EcEHjykqXiJdXlz8KoIAbYc2Vt71NxDKRXHUBu0tMYCATZ+Pc+20oOvTYQk4IY9fUP5YkkfA+3QPolAHnJt2AkENj9/rH1Rd1qeWgDCQBEnQPOl/9QXAJpq105iRdgJKADrARAFClxzD8Dh0Ba66vc5FaYB+h09n/fy9z4BydAJPSRhDPb4KOTTpAAAAntSURBVA5Ie302rvkZzsRZiXmAXr3/W0rlFtr/Qo0JSyTt1zgDMqgQMPGfmAZodwfApMZSuSkdU4PqMlM2Z/8IR0BGqTgnaSGGAVomARObSOWWTMwNjkWFFFlDcAJkZgKQl3wvZgHabgc80xKTg6PxT3r6I8MTgMRMjAJ0Zv+SbpgdfJt1UpD1SxwAGa3SJ+r/ApMArfsFjKsvlQVsBYBLpdvcZ23vHzD7I5Tg3gnwAUYBOrNvIccDQZ3vD13EjI/QN7Q7N2kBJgFaFwQ+3QgDNPp8v7VDInYTZnuEvpMAJN6FSYDuHFzbDyM09Yjf9oGnM9MjdKQEID95IAYB2m8D0CXQND6TIiuLGR6hY+jzUY3PdCbI/ZgE6H1fQGtM0RxWybasc5ndEapeIeAWTAJ0pmxSE4xRf8olYt0uMvL7zOoIVVMluckPYxKgdSHghIYYpO6Fflzkg1At6gDy6vXDJEDrfgBjUjBJXc/2F9kTJWKfxkyOUC0ko+v8aHdu0l6MArRNAMY2wCx1bOdbZGcwgyN04nUAL2MUoO8WAL0AtPvqL8j4MTM3QtGoA8hJvAqjAG2LACc3xTj1YKdErD7M2AhFMwEYe945zkR5ELMALY8BPtcG8ww09n6Hx2RnxinM1gjFYhsgL2kDZgE6UvFSJ0w0uGyVoqy2zNAIxTQBSL4OswAdObCiF0YaPPa45/rnZp/E7IxQfLYB9mEYoBX5yVwJHLwl/yUSsesxKyMUz1UATgOAZuyZ0RxDDUxDn9A7zld/NjMxQh5od27ihZgGaHUR0JJuGKv/2eUu91Pkh5B3kvwGpziT5hcYB+jRAKg+y//+5pB7ZW9B1i+ZfRHyxyrA45gH6ED53PaYrH9ZK4Wh1sy4CPlIu8YmJ9ITALT4+t+SjtH6jw8drmSmRcinKs5JWoiJQKD3/l/ugtn6bp/fvkPW9j6VGRYhP28DcEMgBLnyf3pzkbCF6fqDUreL35vWT5lZEQqARBK+50ykWzETCNzS//gGUrkpDeP1QyOfcCiPAj+EgrgKwJFACJr5j0mRg+v6Yb7ess+9rS+S9mtmUYQCvArgJAH/h7FAUIr+Dq7ugwF7e2HPRNkcOo/ZEyENVJyXeBnmAn6ndEIj58u/PybslfGHQ5NlW2YiMyZCOq0CzE04yZlgd2Ay4NuCv5mtOO7nVXGf2uPH+BHSVyWjk22MBnz31f90I27584ZPHEZS1Y+QIdqdm7Qe0wF/LPc3lH0vdxYppMVvnNkuRdYQzvEjZFotQG5SJ4dKDAi8KfBLkb3PtZH9y3tyvj/uWBslHLJVUTAzIULmJgHPYUbgBWWTmsi+RV252Cd+VEjYniFbs1ox8yGEEvbkJP7amYyLMSTwrslPQ9m/tDsGHTvedq/l3Zbxc2Y8hND/rgLkJY3AiMBr9j7XWiqpAYgW5VJkz5Uiqz/L/Aiho+rwscBtmBB4vi0wvRlJwIkQsXa4X/ub085mZkMIVW8VIDelQ3Fu4gFMCDxfCZjVGiOvGcVut76tViozGUKolklA4oMYEPiB/Uu7YezHW+KPhBZIkfUbidinMXshhE5sK2Bi6slsBYBvbv9jK+DbHHRY5XClFGT8mBkLIRRVlebXa+ZMwOWYELAK4BfTd8/sj6CKHyEU+62AnKQbMCDw/D6A6S1MNf0DjumvlIh9tRQOPocZCSEUv60A98rgpPmYEHhKXrI5HQLDoU+rju2FrqQfP0LIU+3KSTrLmYTfxYjASw6tG6Dzfn7EvYBnq5XKWX2EkL+2AtyjgUkVGBF4hWY3A/7bYaZErGx5fdBZzDAIIZ8nAclXYkTgWSHgsh5BNvx3XcMvsodKwfnNmE0QQoHT7pzEJzAj8CYB6BmcJX3VhU815FH7+NsyE5k5EEKBl4xM+H5xbuJiDAnivgWw0rdbALscs1/mmP69Dn1k+8DTmSkQQlrq81GNz6RJEMS9CHB9fx+Yvf2x24AnHMpzv+7DdnORkd9nVkAIGaOy3ORfFucm7sSYIF7HACsL4toN8Cu36Y5axleNd9RNeuHMX/HmI4SQo91jEpOdyfljDApifjPg5CbRNvhDEgl95Bj8euc/T3P+ebdj9JdIYWZ7qvIRQqga+io3uZUzQX+FSUEsKZ+bWsOv99BbVebuNtQZ416LGw79ViJ2d1WUJ5HUk3l7EULoRFcC8uqlkgRATAsAl/V8uWrf3X7M/VovCg2XsHW5FNoh19SLrBayOXSe7Mj+IW8kQgjFUbtykto4E/UXmBXEgL/yhiGEkJ+TgPzEtiQBEPXrgPOSfsfbhRBCPtfhK4Q/xLggSmxVvSd4sxBCKAD68qn6dZ2JewfmBSfI/uLRyR15oxBCKEDaPb7eT4tzE1/DxKC27M5Nup03CSGEAigZXedHzkT+HGYGtTD/+Sz9I4RQwFWclzTCmdQPYWxQraK/3KS1Mj3pVN4chBDSQCWjk21nci/G4ODYJL/62bjmZ/DGIISQVisBKQ25RAiO8eU/V/IbnMKbghBCGkpN8M5kn4fhwTeodMz/Mfb8EULIAO3OSb7Imfi/xPwMJyfp/dL8pF68EQghZJD25CT+ujg3cTFGaCQHi3OTx331WMpPeBMQQsjU1YDc5GxWA4w64rd+V35ya0Y+QgihhL2j65xXnJM0B4PUushvu9r6YbQjhBA60mrAgOK8pP+HYWrFlpK8pPNFEr7HCEcIIXRUqZMCu3OS7qRvQKD5sjgveSxL/QghhGqskrHnnaOOhzlmUoGh+r2gL2lHcU7izN15yUNKR9drzpE+hBBCJ6zdOfVSDt8pQDthf/BhSV7iiyW5iTeXjE7u8fHEc09jlCKEEIp1IpDHikBcKSvOTd5Y9dyTr9w9JjGZkYgQQsgT7RqbnKj2l6vMCZOOImqF5a+785KmqqX8r3KTW8nchJMYcQghhHylL/Mb/FgZlWNaf8O8a8Wu4rzEVcU5SSPdy5pG1zmbUYUQQigwUgVnjpFlqjvk2R44KuUOmxxyivOSfrMrJymJkYMQQkgbOcZ2ltqrdr9sc5MqDTb8j9Xteo7ZjyjJS+ku05NOZXQghBAyIxkYm5xYtUXg3jewX2OzL1aFeurIpFrKL81v8HOijxBCCDlSpliSl/SH4rzkZx3D/CTAZu8kMsmRqiLI5CtLcpMb02EPIYQQqnZCUK+ZY6LXOYY62+Fd/xp+4k7nny+U5CTeVJJTr5uMrvMjoocQQghFSSVPNvpZcU5ixu6cxLsdw33eYWucjxkWO2ZfpFYoducl3bE7J6X/7vH1fkpkEEIIoThLLa1/lZdST3W7c5KD35bkJd9SnJOU664aqCLDvKRCdQRxd27SR84/vzoK77ltcpW55yatdLcg8pKfUl/06s8szU3uWTYu6Vc8bYSQifr/nV2nXPIDVc4AAAAASUVORK5CYII="
    "width": 40,
    "height": 40,
}
```
```
Response:

{
    "result": "                ########                \n            *##############*            \n          *##################*          \n         ######################         \n        #####+*!################        \n       ###*********##############       \n      ####***+##!***##############      \n     ##############################     \n    ################################    \n    ##########:#########*******#####    \n   ##########***#######**********####   \n   #########*****########****##**####   \n  ##########*****########****#########  \n  ##########*****########****#########  \n  ###########***#########****#########  \n ########################****########## \n #########################+!########### \n ###################################### \n ###################################### \n ###################################### \n ##########+++######################### \n ##########+++###+::################### \n ##########++++#*******:############### \n  #########++++#*!##+****#############  \n  #########++++########**#############  \n  #########++++###########+###########  \n   #######+++++######+++++++#########   \n   ######+++++###+++++++++++#########   \n    ####++++++++++++++++++##########    \n    ###+++++++++++++++##############    \n     ##++++++++++++++##############     \n      #+++++++++++++++############      \n       ++++++++++++++############       \n       ++++++++++++++###########        \n       ++++++++++++++##########         \n       ++++++++++++++########           \n        +++++++++++++######             \n        :++++++++++++##:                \n          ++++++++++                    \n           !+++++                       \n"
}
```

* Note: The JSON result might look a bit weird with the new line characters (\n),
but once we replace the new line characters with actual new lines, the result is as follows:
```
Response:

{
    "result": "                ########                
            *##############*            
          *##################*          
         ######################         
        #####+*!################        
       ###*********##############       
      ####***+##!***##############      
     ##############################     
    ################################    
    ##########:#########*******#####    
   ##########***#######**********####   
   #########*****########****##**####   
  ##########*****########****#########  
  ##########*****########****#########  
  ###########***#########****#########  
 ########################****########## 
 #########################+!########### 
 ###################################### 
 ###################################### 
 ###################################### 
 ##########+++######################### 
 ##########+++###+::################### 
 ##########++++#*******:############### 
  #########++++#*!##+****#############  
  #########++++########**#############  
  #########++++###########+###########  
   #######+++++######+++++++#########   
   ######+++++###+++++++++++#########   
    ####++++++++++++++++++##########    
    ###+++++++++++++++##############    
     ##++++++++++++++##############     
      #+++++++++++++++############      
       ++++++++++++++############       
       ++++++++++++++###########        
       ++++++++++++++##########         
       ++++++++++++++########           
        +++++++++++++######             
        :++++++++++++##:                
          ++++++++++                    
           !+++++                       
"
}
```

#### Discord
* Make sure you replaced the `config.json` values for Discord as outlined in the "Setting up" section.
* Run the discord bot
```
python3 discord_bot.py
```
* Once the bot is ready, you should see it online in your server
![discord_bot_online](./resources/discord_bot_online.png)

* Add an image as an attachment, and tag the discord bot
![discord_bot_attachment](./resources/discord_bot_attachment.png)
![discord_bot_result](./resources/discord_bot_result.png)


