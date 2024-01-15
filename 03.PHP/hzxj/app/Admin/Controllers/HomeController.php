<?php

namespace App\Admin\Controllers;

use App\Admin\Repositories\InspectionResult;
use App\Http\Controllers\Controller;
use App\Models\Department;
use Dcat\Admin\Grid;
use Dcat\Admin\Layout\Column;
use Dcat\Admin\Layout\Content;
use Dcat\Admin\Layout\Row;

class HomeController extends Controller
{
    public function index(Content $content)
    {
        return $content
            ->header('每日巡检结果')
            ->description('')
            ->body(function (Row $row) {
                return Grid::make(new InspectionResult(['department', 'scheduling']), function (Grid $grid) {
                    $grid->selector(function (Grid\Tools\Selector $selector) {
                        $all_departments = Department::all();
                        $department = [];
                        foreach  ($all_departments as $all_department){
                            $department[$all_department->id] = $all_department->name;
                        }
                        $selector->select('department_id', '部门', $department);
                    });
                    $grid->column('id')->sortable();
                    $grid->column('name')->link(function ($value) {
                        return admin_url('inspection-result/'.$this->id);
                    });
                    $grid->column('状态')->display(function (){
                        return $this->inspection_status == 1 ? '正常'  : '<span style="color: red">异常</span>';
                    });
                    $grid->column('department.name', '部门');
                    $grid->column('scheduling.name', '班次');
                    $grid->column('inspector');
                    $grid->column('created_at');
                    $grid->column('updated_at')->sortable();

                    $grid->filter(function (Grid\Filter $filter) {
                        $filter->like('department.name', '部门');
                        $filter->like('created_at', '时间');

                    });
                    $grid->disableBatchDelete();
                    $grid->disableDeleteButton();
                    $grid->disableEditButton();
                    $grid->disableCreateButton();
                    $grid->disableRowSelector();
                });

                });

    }
}
