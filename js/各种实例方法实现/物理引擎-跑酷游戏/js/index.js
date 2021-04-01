var config = {
    type: Phaser.AUTO,
    width: 800,
    height: 400,
    physics: {
        default: 'arcade',
        arcade: {
            gravity: {
                y: 300
            },
            debug: false
        }
    },
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

var game = new Phaser.Game(config); // 创建游戏

var distanceText; // 路程文本
var distance = 0; // 路程
var platforms; // 地面
var player; // 玩家
var enemys; // 敌人们
var gameOver = false; // 游戏结束
var enemy; // 敌人
var enemyTimer; // 敌人计时器
var distanceTimer; // 路程计时器
var cursors; // 按键监听

// 载入资源
function preload() {
    this.load.image('sky', 'assets/sky.png');
    this.load.image('ground', 'assets/platform.png');
    this.load.spritesheet('dude', 'assets/dude.png', {
        frameWidth: 32,
        frameHeight: 48
    });
}

// 将资源展示到画布创建资源
function create() {
    // 添加画布背景
    this.add.image(400, 200, 'sky');
    // 添加分数文本
    distanceText = this.add.text(16, 16, 'Distance: 0m', {
        fontSize: '20px',
        fill: '#000'
    });
    // 添加地面
    platforms = this.physics.add.staticGroup();
    platforms.create(400, 400, 'ground').setScale(3).refreshBody();
    // 添加玩家（精灵）
    player = this.physics.add.sprite(100, 300, 'dude');
    player.setBounce(0); // 设置阻力
    player.setCollideWorldBounds(true); // 禁止玩家走出世界

    // 敌人
    enemys = this.physics.add.group();
    enemys.children.iterate(function (child) {

        child.setCollideWorldBounds(false);
    });

    // 事件
    this.anims.create({
        key: 'left',
        frames: this.anims.generateFrameNumbers('dude', {
            start: 0,
            end: 3
        }),
        frameRate: 10,
        repeat: -1
    });

    this.anims.create({
        key: 'right',
        frames: this.anims.generateFrameNumbers('dude', {
            start: 5,
            end: 8
        }),
        frameRate: 10,
        repeat: -1
    });

    this.anims.create({
        key: 'turn',
        frames: [{
            key: 'dude',
            frame: 4
        }],
        frameRate: 20
    });

    cursors = this.input.keyboard.createCursorKeys();

    // 动态创建敌人
    enemyTimer = setInterval(function () {
        enemy = enemys.create(1000, 300, 'dude');
        enemy.setTint(getColor());
        enemy.anims.play('left', true);
        enemy.setVelocityX(Phaser.Math.Between(-300, -100));
    }, Phaser.Math.Between(4000, 8000))

    distanceTimer = setInterval(function () {
        distance += 1;
        distanceText.setText('Distance: ' + distance + 'm');
    }, 1000)



    this.physics.add.collider(player, platforms); //玩家在地面上
    this.physics.add.collider(enemys, platforms);
    this.physics.add.collider(player, enemys, hitBomb, null, this);

}
// 一直执行
function update() {
    if (cursors.up.isDown && player.body.touching.down) {
        player.setVelocityY(-220);
    } else {
        player.anims.play('right', true);
    }
    if (gameOver) {
        player.setVelocityX(0);
        player.anims.play('turn');
        return;
    }
}

function hitBomb(player, enemys) {
    this.physics.pause();
    clearInterval(enemyTimer);
    clearInterval(distanceTimer);
    player.setTint(0xff0000);
    gameOver = true;
    alert('游戏结束,您跑了' + distance + 'm');
}

function getColor() {
    var color = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"].sort(function(){
        return Math.random() - 0.5
    }).join("").substr(0,6);
    
    return "0x" + color;
}