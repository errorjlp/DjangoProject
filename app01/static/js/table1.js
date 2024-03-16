$(document).ready(function () {
    // 获取表格数据并渲染到表格中
    function renderTableData(data) {
        var tbody = $('table#table-data tbody');
        tbody.empty();

        data.data.forEach(function (item, index) {
            var row = $('<tr>');
            row.append($('<td>').text(item.id));
            row.append($('<td>').text(item.bid));
            row.append($('<td>').text(item.name));
            row.append($('<td>').text(item.cate));
            row.append($('<td>').text(item.year));
            row.append($('<td>').text(item.region));
            row.append($('<td>').text(item.institution));

            tbody.append(row);
        });

        // 更新分页控件的状态
        updatePagination(data.total_pages, data.current_page);
    }

    var currentPage = null;
    var totalPages = null;

    // 更新分页控件的状态
    function updatePagination(serverTotalPages, newCurrentPage) {
        $('.total').text(`共${serverTotalPages}页`);
        $('.current').text(`当前为第${newCurrentPage}页`);
        currentPage = newCurrentPage;
        totalPages = serverTotalPages;

        // 给分页按钮添加点击事件监听器
        bindPaginationButtonEventsOnce();
    }

    // 跳转到指定页码
    function gotoPage(targetPage) {
        if (targetPage > 0 && targetPage <= totalPages) {
            $.ajax({
                url: `/table1api/?page=${targetPage}`,
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    renderTableData(data);
                    updatePagination(data.total_pages, targetPage);
                },
                error: function (xhr, status, error) {
                    console.error(error);
                }
            });
        } else {
            alert('请输入有效的页码！');
        }
    }

    var paginationButtonsBound = false;

    // 绑定分页按钮事件（仅在首次加载时执行）
    function bindPaginationButtonEventsOnce() {
        if (!paginationButtonsBound) {
            $('#bt1').click(function () { // 首页
                gotoPage(1);
            });

            $('#bt2').click(function () { // 上一页
                var currentPage = getCurrentPage();
                if (currentPage > 1) {
                    gotoPage(currentPage - 1);
                }
            });

            $('#bt3').click(function () { // 下一页
                var currentPage = getCurrentPage();
                if (currentPage < totalPages) {
                    gotoPage(currentPage + 1);
                }
            });

            $('#bt4').click(function () { // 尾页
                gotoPage(totalPages);
            });

            $('button[type="submit"]').click(function () { // 跳转按钮
                var targetPage = parseInt($('input[type="number"]').val());
                gotoPage(targetPage);
            });

            paginationButtonsBound = true;
        }
    }

    // 获取当前页码
    function getCurrentPage() {
        return currentPage;
    }

    // 初始加载表格数据
    function getTableData() {
        $.ajax({
            url: '/table1api/',
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                renderTableData(data);
                updatePagination(data.total_pages, data.current_page);
                bindPaginationButtonEventsOnce(); // 在首次加载数据后绑定事件
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        });
    }

    // 加载表格数据
    getTableData();

    // 添加分页功能
    $(document).on('click', '.pagination a', function (e) {
        e.preventDefault();
        var page = $(this).attr('href').split('page=')[1];
        gotoPage(page);
    });
});