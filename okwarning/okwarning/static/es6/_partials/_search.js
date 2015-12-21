(() => {
  $(document).ready(() => {
    var form = $('section#search form');
    var input_query = form.find('input#query');

    form.on('submit', (event) => {
      var url = '/api/history/';
      var query = input_query.val();
      var data = {
        'url': query
      };

      $.ajax({
        url: url,
        type: 'POST',
        data: data,
      }).done((data) => {
        input_query.val('');
      }).fail((data) => {
      });

      return false;
    });
  });
})();
