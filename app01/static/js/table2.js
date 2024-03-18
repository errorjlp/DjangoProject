$(document).ready(function () {
    // 获取表格数据并渲染到表格中
    function renderTableData(data) {
        var tbody = $('table#table-data tbody');
        tbody.empty();

        data.data.forEach(function (item, index) {
            var row = $('<tr>');
            row.append($('<td>').text(item.id));
            row.append($('<td>').text(item.name));
            row.append($('<td>').text(item.gender));
            row.append($('<td>').text(item.nation));
            row.append($('<td>').text(item.category));
            row.append($('<td>').text(item.bid));
            row.append($('<td>').text(item.pname));
            row.append($('<td>').text(item.region));

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
                url: `/table2api/?page=${targetPage}`,
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

    const DEFAULT_GENDER = '性别';
    const DEFAULT_CATEGORY = '类别';
    const DEFAULT_REGION = '所属地区';
    let filterSubmitBtn = $('button.filter-submit'); // 筛选按钮的class为'.filter-submit'
    let genderFilter = $('#gender');
    let cateFilter = $('#category');
    let regionFilter = $('#region');

    // 给筛选按钮添加点击事件
    filterSubmitBtn.click(function () {
        let gender = genderFilter.val();
        let category = cateFilter.val();
        let region = regionFilter.val();
        // 检查筛选条件是否为默认值
        gender = gender !== DEFAULT_GENDER ? gender : null;
        category = category !== DEFAULT_CATEGORY ? category : null;
        region = region !== DEFAULT_REGION ? region : null;
        // 创建筛选参数对象，只包含非默认值的筛选条件
        const params = {};
        if (gender) params.gender = gender;
        if (category) params.category = category;
        if (region) params.region = region;
        // 只发送筛选条件，不触发页码跳转
        console.log(params)

        loadFilteredTableData(params);
    });
    // 添加重置筛选按钮的点击事件监听器
    let resetFilterBtn = $('.reset-filter');
    resetFilterBtn.click(function () {
        // 清空筛选条件输入框
        genderFilter.val('性别');
        cateFilter.val('类别');
        regionFilter.val('所属地区');

        // 重新加载初始表格数据
        initialLoadTableData();
    });

    // 加载经过筛选的表格数据
    function loadFilteredTableData(params) {

        $.ajax({
            url: '/table2api/',
            type: 'GET',
            data: params,
            dataType: 'json',
            success: function (data) {
                renderTableData(data);
                updatePagination(data.total_pages, data.current_page);
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        });
    }
    // 初始加载表格数据
    function initialLoadTableData() {
        getTableData(null, null, null);
    }
    // 初始加载表格数据
    function getTableData(gender, category, region) {
        let params = {
            gender: gender,
            category: category,
            region: region
        };

        // 移除无效的筛选参数（即值为空的筛选条件）
        params = Object.entries(params).reduce((acc, [key, value]) => value ? {...acc, [key]: value} : acc, {});

        $.ajax({
            url: '/table2api/',
            type: 'GET',
            data: params,
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

    // 在文档加载完成后首先进行初始化加载
    $(document).ready(function () {
        // ...
        initialLoadTableData();
        // ...
    });
    // 加载表格数据
    getTableData();

    // 添加分页功能
    $(document).on('click', '.pagination a', function (e) {
        e.preventDefault();
        var page = $(this).attr('href').split('page=')[1];
        gotoPage(page);
    });
});