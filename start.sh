if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/CyberTG/SneakBot.git /SneakBot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /SneakBot
fi
cd /SneakBot
pip3 install -U -r requirements.txt
echo "𝙎𝙏𝘼𝙍𝙏𝙄𝙉𝙂..☀️"
python3 bot.py
