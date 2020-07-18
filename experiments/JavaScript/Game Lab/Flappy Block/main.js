let stateManager = {

    preload: function () {
        game.load.image('yellow', 'assets/yellow.png');
        game.load.image('green', 'assets/green.png');
    },

    create: function () {
        // Game configuration
        game.stage.backgroundColor = '#000080';
        game.physics.startSystem(Phaser.Physics.ARCADE);

        // Character configuration
        this.hero = game.add.sprite(100, 245, 'yellow');
        game.physics.arcade.enable(this.hero);
        this.hero.body.gravity.y = 1000;

        // System configuration
        let spaceKey = game.input.keyboard.addKey(Phaser.Keyboard.SPACEBAR);
        spaceKey.onDown.add(this.jump, this);

        // Enemies configuration
        this.enemies = game.add.group();

        // Game configuration
        this.timer = game.time.events.loop(1500, this.addRowOfEnemies, this);
    },

    update: function () {
        if (this.hero.y < 0 || this.hero.y > 400) {
            this.restart();
        }

        game.physics.arcade.overlap(this.hero, this.enemies, this.restart, null, this);
    },

    jump: function () {
        this.hero.body.velocity.y = -350;
    },

    restart: function () {
        game.state.start('main');
    },

    addEnemy: function (x, y) {
        // Enemy creation
        let enemy = game.add.sprite(x, y, 'green');
        this.enemies.add(enemy);
        game.physics.arcade.enable(enemy);

        // Enemy configuration
        enemy.body.velocity.x = -200;
        enemy.checkWorldBounds = true;
        enemy.outOfBoundsKill = true;
    },

    addRowOfEnemies: function () {
        let hole = Math.floor(Math.random() * 5) + 1;
        for (let index = 0; index < 8; index++) {
            if (index != hole && index != hole + 1) {
                this.addEnemy(400, index * 60 + 10);
            }
        }

    }
}


let game = new Phaser.Game(400, 490);
game.state.add('main', stateManager);
game.state.start('main');