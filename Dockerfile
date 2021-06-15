FROM  ilhammansiz17/ilham-mansiez-petercord:Petercord-Userbot

RUN git clone -b master https://github.com/ilhammansiz/PandaUserbot /root/Panda
WORKDIR /root/Panda

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/Panda/bin:$PATH"

CMD ["python3","-m","Panda"]
