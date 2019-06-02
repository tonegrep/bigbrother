 $(document).ready(function () {
    $('#errorModal').modal('show');
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });
});