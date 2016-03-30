var Bookshelf = require("./db").bookshelf;

//Bookshelf.plugin("visibility");
// User model
var User = Bookshelf.Model.extend({
    tableName: 'users'
});

// Post model
var Post = Bookshelf.Model.extend({
    tableName: 'posts',
    hasTimestamps: true,
    category: function() {
        return this.belongsTo(Category, 'category_id');
    },
    tags: function() {
        return this.belongsToMany(Tag);
    },
    author: function() {
        return this.belongsTo(User);
    }
});

// Category model
var Category = Bookshelf.Model.extend({
    tableName: 'categories',
    posts: function() {
        return this.hasMany(Post, 'category_id');
    }
});

// Tag model
var Tag = Bookshelf.Model.extend({
    tableName: 'tags',
    posts: function() {
        return this.belongsToMany(Post);
    }
});


module.exports.User= User;