(function (){
    IPython.CodeCell.prototype._handle_set_next_input = function (payload) {
        var data = {
            cell: this,
            text: payload.text,
            replace: payload.replace,
            clear_output: payload.clear_output,
        execute: payload.execute
        };
        this.events.trigger('set_next_input.Notebook', data);
    };

    var that = IPython.notebook;
    // Out with the old, in with the new
    that.events.unbind("set_next_input")
    that.events.on('set_next_input.Notebook', function (event, data) {
            if (data.replace) {
                data.cell.set_text(data.text);
                if (data.clear_output !== false) {
                  // default (undefined) is true to preserve prior behavior
                  data.cell.clear_output();
                }
            } else {
                var index = that.find_cell_index(data.cell);
                var new_cell = that.insert_cell_below('code',index);
                new_cell.set_text(data.text);
            }
        
        if (data.execute && data.execute === true) {
        new_cell.execute();
        } else {
        that.dirty = true;
        }
    });
})()