<?php

namespace App\Models;

use Dcat\Admin\Traits\HasDateTimeFormatter;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Database\Eloquent\SoftDeletes;
use Illuminate\Database\Eloquent\Model;

class InspectionResult extends Model
{
	use HasDateTimeFormatter;
    use SoftDeletes;

    protected $fillable = [
        'name',
        'department_id',
    ];

    protected $table = 'inspection_results';

    public function projects_result(): HasMany{
        return $this->hasMany(ProjectResult::class);
    }

    public function department(): BelongsTo
    {
        return $this->belongsTo(Department::class);
    }

    public function scheduling(): BelongsTo
    {
        return $this->belongsTo(Scheduling::class);
    }
}
