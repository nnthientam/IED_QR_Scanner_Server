from flask import Flask, redirect, url_for, request, render_template, session
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def findIED():
    
    iedID = request.args.get('id',None)

    conn = sqlite3.connect('IEDData.db')
    cur = conn.cursor()

    if iedID:
        cur.execute('SELECT * FROM IEDDetail WHERE IEDId = ?',(iedID,))
        try:
            data = cur.fetchone()
            subs = str(data[2])
            bay = str(data[3])
            ied = str(data[4])
            serial = str(data[5])
            version = str(data[6])
            IP = str(data[7])
            Subnet = str(data[8])
            DefaultGW = str(data[9])
            GPS1 = str(data[10])
            GPS2 = str(data[11])
            user = str(data[12])
            password = str(data[13])
            protocol = str(data[14])
            notes = str(data[15])
            notes = notes.replace('\n','<br>')

            return render_template(
                'index.html',
                subs = subs,
                bay = bay,
                ied = ied,
                serial = serial,
                version = version,
                IP = IP,
                Subnet = Subnet,
                DefaultGW = DefaultGW,
                GPS1 = GPS1,
                GPS2 = GPS2,
                user = user,
                password = password,
                protocol = protocol,
                notes = notes)
        except Exception as e:
            print(e)
            return render_template('error.html')
    else:
        return render_template('error.html')
app.run(debug=True, host='10.72.92.67')